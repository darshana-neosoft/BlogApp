from django.shortcuts import render,redirect,render_to_response
from django.template import RequestContext
import MySQLdb
import json
import pdb
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse
from bloggerapp.models import *

# Create your views here.
def index(request):
	return render(request,"login.html")

def signup_page(request):
	return render(request,"signup.html")

def blog_page(request):
	#pdb.set_trace()
	try:
		blog_list =[]
		user_name = request.session['login_user']
		user_id = request.session['user_id']
		blog_objs = Blog.objects.all()
		for blog in blog_objs:
			blog_owner = blog.blog_owner.user_first_name + " " + blog.blog_owner.user_last_name
			blog_comments = BlogComment.objects.filter(blog_id =blog.blog_id).count()
			blog_likes = BlogLikes.objects.filter(blog_id =blog.blog_id).count()
			blog = {'blog_id':blog.blog_id,'blog_title':blog.blog_name,'blog_content':blog.blog_content,
			'blog_owner':blog_owner,'blog_comments':blog_comments,'blog_likes':blog_likes}
			blog_list.append(blog)
		#print blog_list
		data = {'success':'true','user_id':user_id,'name':user_name,'blog_list':blog_list}
		#print data
	except Exception,e:
		print e
		data = {'success':'false'}
	return render(request,'blogs.html',data)

@csrf_exempt
def user_login(request):
	#pdb.set_trace()
	print "HI",request.POST
	if request.POST:
		email = request.POST.get("email")
		password = request.POST.get("password")
		try:
			user = authenticate(username = email,password=password)
			if user is not None:
				if user.is_active:
					user_obj = BlogUser.objects.get(user_email_id = user.username)
					request.session['login_user'] = user_obj.user_first_name + "" + user_obj.user_last_name
					request.session['user_id'] = user_obj.user_id
					login(request,user)
					return redirect('/blog-page/')
				else:
					message = "User is not active"
					return render_to_response('login.html',dict(message=message),context_instance=RequestContext(request))
			else:
				print 'Logs:------Invalid Username or Password---------'
		        message = 'Invalid Username or Password'
		        return render_to_response('login.html',dict(message=message),context_instance = RequestContext(request))
		except User.DoesNotExist:
			print 'login error logs:- user does not exist'
			message = 'User Not Exit'
		except MySQLdb.OperationalError, e:
			print 'login error logs db:-', e
			message = 'Internal Server Error'
		except Exception, e:
			print 'login error logs e:-', e
			message = 'Internal Server Error'
			return render_to_response('login.html', dict(message=message), context_instance=RequestContext(request))


@csrf_exempt
def user_signup(request):
	print "Hi"
	if request.POST:
		try:
			user_obj = BlogUser(
				username  = request.POST.get("email"),
				user_first_name  = request.POST.get("firstName"), 
				user_last_name   = request.POST.get("lastName"),
				user_email_id  =  request.POST.get("email"),
				user_mobile_no = request.POST.get("mobileNumber"),
				created_by  =request.POST.get("firstName") + " " + request.POST.get("lastName"),
				updated_by =request.POST.get("firstName") + " " + request.POST.get("lastName"),
		        created_date =datetime.now(),
		        row_status ="ACTIVE",
			)
			user_obj.save()
			user_obj.set_password(request.POST.get("confpass"))
			user_obj.save()
			data = {
            	'success': 'true',
            	'message': 'User Signed up successfully'
        	}
		except IntegrityError, e:
			print "Views => IntegrityError => user_signup: ", e
			data = {
            	'success': 'false',
            	'message': 'User already exist'
        	}
 		except Exception, e:
 			print "Views => Exception => user_signup: ", e
 			data = {
	            'success': 'false',
	            'message': 'Sever Error'
	        }
    	return HttpResponse(json.dumps(data), content_type='application/json')
		
		
@csrf_exempt
def add_blog(request):
	if request.POST:
		try:
			blog_obj = Blog(
				blog_name = request.POST.get("blog_title"),
				blog_content = request.POST.get("blog_content"),
				blog_owner = BlogUser.objects.get(user_id=request.session['user_id']),
				created_by  =request.session['login_user'],
				updated_by = request.session['login_user'],
		        created_date =datetime.now(),
		        row_status = "ACTIVE",
			)
			blog_obj.save()
			data = {'success':'true','message':'Blog added successfully'}
		except Exception,e:
			print e
			data = {'success':'false','message':'Error'}
		return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def add_blog_like(request):
	try:
		if request.POST:
			blog_id = request.POST.get("blog_id")
			user_id = request.POST.get("user_id")
			blog_like_obj = BlogLikes(
				blog_id  =  Blog.objects.get(blog_id = blog_id),
				blog_like_owner = BlogUser.objects.get(user_id=user_id),
				created_by  =request.session['login_user'],
				updated_by = request.session['login_user'],
		        created_date =datetime.now(),
		        row_status = "ACTIVE",
				)
			blog_like_obj.save()
			blog_likes = BlogLikes.objects.filter(blog_id =blog_id).count()
			blog_likes = str(blog_likes) +" " +"likes"
			data = {'success':'true','blog_likes':blog_likes}
	except IntegrityError,e:
		data = {'success':'false'}
	except Exception,e:
		print e
		data = {'success':'false','message':'Error'}
	return HttpResponse(json.dumps(data), content_type='application/json')


def blog_details(request):
	try:
		comment_list =[]
		user_name = request.session['login_user']
		user_id = request.session['user_id']
		blog_id = request.GET.get("blog_id")
		blog_obj = Blog.objects.get(blog_id = blog_id)
		blog_owner = blog_obj.blog_owner.user_first_name + " " + blog_obj.blog_owner.user_last_name
		blog_comments = BlogComment.objects.filter(blog_id =blog_obj.blog_id).count()
		blog_likes = BlogLikes.objects.filter(blog_id =blog_obj.blog_id).count()
		blog_comment_objs = BlogComment.objects.filter(blog_id =blog_obj.blog_id)
		for comment in blog_comment_objs:
			comment_owner = comment.blog_comment_owner.user_first_name + " " + comment.blog_comment_owner.user_last_name
			comments ={'content':comment.blog_comment_content,'owner':comment_owner,'date':comment.created_date}
			comment_list.append(comments)
		data = {'name':user_name,'comment_list':comment_list,'user_id':user_id,'blog_id':blog_obj.blog_id,'blog_title':blog_obj.blog_name,'blog_content':blog_obj.blog_content,
		'blog_owner':blog_owner,'blog_comments':blog_comments,'blog_likes':blog_likes}
	except Exception,e:
		print e
		data = {'data':'Null'}
	return render(request,'blog-details.html',data)



@csrf_exempt
def add_blog_comment(request):
	try:
		if request.POST:
			blog_id = request.POST.get("blog_id")
			user_id = request.POST.get("user_id")
			blog_comment = request.POST.get("blog_comment")
			blog_comment_obj = BlogComment(
				blog_id  =  Blog.objects.get(blog_id = blog_id),
				blog_comment_owner = BlogUser.objects.get(user_id=user_id),
				blog_comment_content = blog_comment,
				created_by  =request.session['login_user'],
				updated_by = request.session['login_user'],
		        created_date =datetime.now(),
		        row_status = "ACTIVE",
				)
			blog_comment_obj.save()
			blog_comments = BlogComment.objects.filter(blog_id =blog_id).count()
			blog_comments = str(blog_comments) +" " +"comments"
			data = {'success':'true','blog_comments':blog_comments}
	except Exception,e:
		print e
		data = {'success':'false','message':'Error'}
	return HttpResponse(json.dumps(data), content_type='application/json')


def log_out(request):
	logout(request)
	return redirect("/")
	
    