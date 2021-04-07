    var username = [['ahmed',123,true],['ali',133,false],['jaber',223,false],['nasser',433,false]];
    var products = [[123,'item1',2,2],[124,'item2',10.5,1],[134,'item3',50.5,1],[234,'item4',60.5,1]];
$('document').ready(function () {

   
    var str = "";
    var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                str += this.responseText;
                username = JSON.parse(str);
            }
        };
        xmlhttp.open("GET", "getUser.php");
        xmlhttp.send();
    var str3 = "";

    var xmlhttp3 = new XMLHttpRequest();
        xmlhttp3.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                str3 += this.responseText;
                products = JSON.parse(str3);
                //alert(str3)
            }
        };
        xmlhttp3.open("GET", "productManage.php?manage=0");
        xmlhttp3.send();

   
         
        

    




    var content = document.getElementById('content');
    $('#users').click(function () {
        
        

        var element = "";
        for(i=0;i<username.length;i++){
            var name = username[i][1];
            var id = username[i][0];
            var blocked = username[i][5];
            var btncolor = 'btn-danger';
            var btnTxt = 'block';
            element += "<span><div class='card d-inline-block'> <div class='card-body'> "+name+ "</div> <div class='card-body'>  </div>"
            if (blocked==2){
                btncolor = 'btn-success'
                btnTxt = 'unblock'
            }else {
                btncolor = 'btn-danger'
                btnTxt = 'block'
            }

            var blockbtn = `<buttom onclick='block(${id},${blocked},${i});' id='block${id}' class='btn ${btncolor}'>${btnTxt}</buttom>`
            var delbtn = `<buttom onclick='$(this).parents("span").hide(); del(${id});' id='del${id}' class='deluser btn btn-danger '>Delete</buttom>`

            element += "<div class='card-footer'>"+blockbtn+ delbtn+ "</div></div></span>"
        }
        content.innerHTML = element;

    });

    var content = document.getElementById('content');
    $('#products').click(function () {
        var element = "";
        for(i=0;i<products.length;i++){
            var name = products[i][1];
            var id = products[i][0];
            var desc = products[i][3];

            var price = Number(products[i][4]);
            
            //
            //   <img src="test.png" alt="Just testing.">
            //

            var image = `<object data="images/products/${id}.png" height=50><img height="50px" src=" images/products/default.png "  /></object>`;
            name = `<p>${name}</p>`
            price = `<p>${price} $$</p>`

            element += `<span><div class='card d-inline-block'> <div class='card-body'> ${name+image + price} </div> <div class='card-body'>  </div>`

            //var delbtn = "<buttom id='del"+id+"' class='btn "+"btn-danger"+"'>"+"Delete"+"</buttom>"
            var delbtn = `<buttom onclick='$(this).parents("span").hide(); delPr(${id});' id='del${id}' class='deluser btn btn-danger '>Delete</buttom>`

            //delPr
            element += "<div class='card-footer'>"+ delbtn+ "</div></div></span>"
        }
        content.innerHTML = element;

    }); 
    
    


});

function del(p1) {
    var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     // alert(this.responseText);
    }
  };
  xhttp.open("GET", `removeUser.php?userID=${p1}&status=3`, true);

  xhttp.send();


  
    
}
function delPr(p1) {
    var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     // alert(this.responseText);
    }
  };
  xhttp.open("GET", `productManage.php?productId=${p1}&manage=0`, true);

  xhttp.send();


  
    
}
function block(id,st,index) {
    
    if (st == 2){
    st = 1;   
  }else {
    st = 2;
  }
    
    var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     
    }
  };
  
  xhttp.open("GET", `removeUser.php?userID=${id}&status=${st}`, true);
  xhttp.send();
  username[index][5]=st;

        
        

        var element = "";
        for(i=0;i<username.length;i++){
            var name = username[i][1];
            var id = username[i][0];
            var blocked = username[i][5];
            var btncolor = 'btn-danger';
            var btnTxt = 'block';
            element += "<span><div class='card d-inline-block'> <div class='card-body'> "+name+ "</div> <div class='card-body'>  </div>"
            if (blocked==2){
                btncolor = 'btn-success'
                btnTxt = 'unblock'
            }else {
                btncolor = 'btn-danger'
                btnTxt = 'block'
            }

            var blockbtn = `<buttom onclick='block(${id},${blocked},${i});' id='block${id}' class='btn ${btncolor}'>${btnTxt}</buttom>`
            var delbtn = `<buttom onclick='$(this).parents("span").hide(); del(${id});' id='del${id}' class='deluser btn btn-danger '>Delete</buttom>`

            element += "<div class='card-footer'>"+blockbtn+ delbtn+ "</div></div></span>"
        }
        content.innerHTML = element;

    
       
}



