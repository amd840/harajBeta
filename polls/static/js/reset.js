var code1 = 0;
$('document').ready(function () {
	$('#emailsend').click( function (){
		code1 = Math.random();
		$.ajax({
			type: "POST",
			url: "./resetpassword.php",
			data: { url: code1 },success: function(result){

        		}
			});
			

		
		$('#url').val(code1);
	})


});