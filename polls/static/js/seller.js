var products = [[123,'item1',2,2],[124,'item2',10.5,1],[134,'item3',50.5,1],[234,'item4',60.5,1]];
var str = ""
var element = "";
var thecontent = $('section');

    var xmlhttp2 = new XMLHttpRequest();
        xmlhttp2.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {

                str += this.responseText;
                products = JSON.parse(str);
                add();


                
            }
        };
        xmlhttp2.open("GET", "./productManage.php");
        xmlhttp2.send();

        
$('document').ready(function () {
    var id = 0

    $("#ss").on('submit',(function(e) {
  e.preventDefault();
  $.ajax({
         url: "./productManage.php?manage=true",
   type: "POST",
   data:  new FormData(this),
   contentType: false,
         cache: false,
   processData:false,
   beforeSend : function()
   {
    //$("#preview").fadeOut();
    $("#err").fadeOut();
   },
   success: function(data)
      {
    if(data=='invalid')
    {
     // invalid file format.
     $("#err").html("Invalid File !").fadeIn();
    }
    else
    {
     // view uploaded file.
     $('#myModal').modal('hide');
      $.ajax({
    url: "test.php",success: function(result){
            id = result;
        }});
     var name = $("#itemName").val();
        var price = Number($("#itemPrice").val());
        var imgpath = $('#itemImage').val();
        var amount = $('#itemAmount').val();
        var des = $('#itemDes').val();
        var image = `<object data="./images/products/${id}.png" height=50px><img height="50px" src="./images/products/default.png"/></object>`;
        name = `<p>${name}</p>`
        price = `<p>${price} $</p>`
        amount = `<p>amount: ${amount}</p>`
        des = `<p>${des}</p>`


        element += `<div class='card d-inline-block'> <div class='card-body'> ${name+image+ des+ price + amount} </div> <div class='card-body'>  </div>`

        var delbtn = "<buttom id='del"+id+"' class='btn "+"btn-danger"+"'>"+"Delete"+"</buttom>"

        element += "<div class='card-footer'>"+ delbtn+ "</div></div>"
        thecontent.html(element);

     $("#ss")[0].reset(); 
    }
      },
     error: function(e) 
      {
    $("#err").html(e).fadeIn();
      }          
    });
     
            


 }));

    


    
   

    
    
/*
    $('#addit').click(function () {

            var name = $("#itemName").val();
            var id = 26
            var price = Number($("#itemPrice").val());
            var imgpath = $('#itemImage').val();
            var amount = $('#itemAmount').val();
            var des = $('#itemDes').val();
            //var formData = new FormData($(#ss));
            
            var xmlhttp = new XMLHttpRequest();
            var message = "";
            $.ajax({
                type: "POST",
                //enctype="multipart/form-data",
                url: "test.php",
                data: { itemName: name, itemImage: imgpath },
                success: function(result){
                    alert(result)
                    }
                });

            /*xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    alert(this.responseText);
                }
                };
            //xmlhttp.open("POST",`productManage.php?itemName=${name}&itemDes=${des}&itemPrice=${price}&itemImage='${imgpath}'&itemAmount=${amount}&proSeller=${id}&manage=true`);
            //xmlhttp.send();


            
            //   <img src="test.png" alt="Just testing.">
            //<picture> <source srcset="images/products/${id}.png""><img src="images/products/default.png" alt="Flowers"></picture>

            var image = `<object data="images/products/${id}.png" height=50px><img height="50px" src="images/products/default.png"/></object>`;
        name = `<p>${name}</p>`
        price = `<p>${price} $</p>`
        amount = `<p>amount: ${amount}</p>`
        des = `<p>${des}</p>`


        element += `<div class='card d-inline-block'> <div class='card-body'> ${name+image+ des+ price + amount} </div> <div class='card-body'>  </div>`

            var delbtn = "<buttom id='del"+id+"' class='btn "+"btn-danger"+"'>"+"Delete"+"</buttom>"

            element += "<div class='card-footer'>"+ delbtn+ "</div></div>"
        thecontent.html(element);



    });*/





    

});
function add(){
    element = "";
    for(i=0;i<products.length;i++){
       
        //

        var id = Number(products[i][0]);

        var amount = Number(products[i][4]);
            amount = `<p>amount: ${amount}</p>`

        var desc = products[i][3];
            desc = `<p>${desc}</p>`

        var image = `<object data="./images/products/${id}.png" height=50px><img height="50px" src="./images/products/default.png" /></object>`;

        var name = `<p>${products[i][1]}</p>`;
        var price = `<p>${products[i][2]} $</p>`;

        element += `<span><div class='card d-inline-block'> <div class='card-body'> ${name+image+ desc+ price + amount} </div> <div class='card-body'>  </div>`

        var delbtn = `<buttom id='del${id}' onclick='del(${id});' class='btn btn-danger'>Delete</buttom>`

        element += "<div class='card-footer'>"+ delbtn+ "</div></div></span>"

    }
    thecontent = $('section');

    
    
    thecontent.html(element);
    

    


};
function del(p1) {
    if (confirm("Delete confirmation!")) {
        $("#del"+p1).parents("span").hide();
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     // alert(this.responseText);
    }
  };
  xhttp.open("GET", './productManage.php?productId='+p1, true);

  xhttp.send();
} else {
}
    


  
    
}

