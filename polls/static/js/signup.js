$(document).ready(function(){

    $('#signup').click(function(){
        var pass1 = document.getElementById('pass1').value;
        var pass2 = document.getElementById('pass2').value;
        var info = document.getElementById('regInfo');
        var email = document.getElementById('email');
        
        

    if((pass1!=pass2)) {
        alert('Your password doesn\'t match');


    }
    else if (!info.checkValidity()){
            alert("complite your information");
            if(!email.checkValidity()){
                email.style.background = '#dc3545';
            }else {
                email.style.background = '#bee5eb';
            }
    }else {
        //window.open("index.html",'_self')
        info.submit();
    }
});

});