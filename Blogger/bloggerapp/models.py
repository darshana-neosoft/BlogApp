from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

USER_IMAGE  = "user_image"
ROW_STATUS = (('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'))


class BlogUser(User):
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=250, blank=True, null=False)
    user_last_name = models.CharField(max_length=250, blank=True, null=False)
    user_email_id = models.CharField(max_length=250, blank=True, null=False)
    user_mobile_no = models.CharField(max_length=50, blank=True, null=False)
    user_image = models.FileField(upload_to=USER_IMAGE, max_length=500, null=True, blank=True)
    row_status = models.CharField(max_length=50, choices=ROW_STATUS, default='ACTIVE')
    created_by = models.CharField(max_length=250, blank=True, null=False)
    updated_by = models.CharField(max_length=250, blank=True, null=False)
    created_date = models.DateTimeField(default=datetime.now())
    updated_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.user_first_name + ' ' + self.user_last_name)

class Blog(models.Model):
	blog_id   = models.AutoField(primary_key=True)
	blog_name  = models.CharField(max_length=600, blank=True, null=False)
	blog_content = models.CharField(max_length=5000, blank=True, null=False)
	blog_owner = models.ForeignKey(BlogUser, null=True, default=None)
	row_status = models.CharField(max_length=50, choices=ROW_STATUS, default='ACTIVE')
	created_by = models.CharField(max_length=250, blank=True, null=False)
	updated_by = models.CharField(max_length=250, blank=True, null=False)
	created_date = models.DateTimeField(default=datetime.now())
	updated_date = models.DateTimeField(null=True, blank=True)
	def __unicode__(self):
		return unicode(self.blog_name)

class BlogComment(models.Model):
	blog_comment_id   = models.AutoField(primary_key=True)
	blog_comment_name  = models.CharField(max_length=600, blank=True, null=False)
	blog_comment_content = models.CharField(max_length=5000, blank=True, null=False)
	blog_id = models.ForeignKey(Blog, null=True, default=None)
	blog_comment_owner = models.ForeignKey(BlogUser, null=True, default=None)
	row_status = models.CharField(max_length=50, choices=ROW_STATUS, default='ACTIVE')
	created_by = models.CharField(max_length=250, blank=True, null=False)
	updated_by = models.CharField(max_length=250, blank=True, null=False)
	created_date = models.DateTimeField(default=datetime.now())
	updated_date = models.DateTimeField(null=True, blank=True)


class BlogLikes(models.Model):
	blog_like_id   = models.AutoField(primary_key=True)
	blog_id = models.ForeignKey(Blog, null=True, default=None)
	blog_like_owner = models.ForeignKey(BlogUser, null=True, default=None)
	row_status = models.CharField(max_length=50, choices=ROW_STATUS, default='ACTIVE')
	created_by = models.CharField(max_length=250, blank=True, null=False)
	updated_by = models.CharField(max_length=250, blank=True, null=False)
	created_date = models.DateTimeField(default=datetime.now())
	updated_date = models.DateTimeField(null=True, blank=True)
	class Meta:
		unique_together = ('blog_id', 'blog_like_owner')

# Create your models here.
