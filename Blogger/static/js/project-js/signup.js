
$("#signup").submit(function(e) 
{
	alert("HI");
var formData = new FormData(this);
$.ajax({
    			type : 'POST',
    			url : '/user-signup/',
    			data : formData,
    			
    			success: function(response) {
    				console.log(response);
        			if(response.success=='true'){
                        alert(response.message);
        			         window.location.href = '/blog-page/'
        	
        			}
        			if(response.success=='false'){
        				alert(response.message);
        			}
    			},
    			error: function(response){
           			alert(response.message);
                },
		    })
});