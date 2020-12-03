$(document).ready(function(){ 

    
    $('#like_button').on('click',function(){
       
        $.post('/like_post',
            {
                post_id: $('#post_id').val(),
                csrfmiddlewaretoken:CSRFTOKEN
            }
        )
        .done(function(data){
            
            if (data.data == 100){
                
                $('#like_count').html(data.like);
                $("#like").addClass("text-danger");
                $("#like").removeClass("text-primary");
            }else{

                console.log('an error occured');
            }

        })
        .fail(function(){

        })
    })

    $('#contact_submit').on('click',function(){
        var l = Ladda.create(document.querySelector('#contact_submit'));
        l.start();

        $.post('/contact',
            {
               // client_name: $('#name').val(),
                email:$('#email').val(),
                message:$('#message').val(),
                csrfmiddlewaretoken:CSRFTOKEN
            }
        )
        .done(function(data){
            
            if (data.data == 100){
                swal('success',data.alert,'success')
                $('#name').val("");
                $('#email').val('');
                $('#message').val('')
                
                l.stop();
                // window.location.reload();
            }else{
                swal("Error!",data.alert,'error')
                l.stop();
                console.log('an error occured');
            }

        })
        .fail(function(){

        })
    })

    $('#subscribe').on('click',function(){

       
       // var l = Ladda.create(document.querySelector('#subscribe_submit'));
       // l.start();

        $.post('/subscribe',
            {
               
                email:$('#email').val(),
               
                csrfmiddlewaretoken:CSRFTOKEN
            }
        )
        .done(function(data){
            
            if (data.data == 100){
                //swal('success',data.alert,'success')
                // $('#name').val("");
                $('#email').val('');
                
                
                //l.stop();
                 window.location.reload();
            }else{
               // swal("Error!",data.alert,'error')
                //l.stop();
                console.log('an error occured');
            }

        })
        .fail(function(){

        })
    })

    $('#comment_submit').on('click',function(){
        

        $.post('/detail/'+$("#post_id").val()+"/",
            {
                
                opinion:$('#comment').val(),
      
                csrfmiddlewaretoken:CSRFTOKEN
            }
        )
        .done(function(data){
            
            if (data.data == 100){
                //swal('success',data.alert,'success')
                alert('success')
                
                l.stop();
                window.location.reload();
            }else{
                alert('Error')
               
                console.log('an error occured');
            }

        })
        .fail(function(){

        })
    })



    
})







