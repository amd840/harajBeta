    var products = [[11,'name1',45,2,'path.jpg'],[22,'name2',34,4,'path.jpg']];
     var totalCost = 0

    var str = "";
    var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                str += this.responseText;
                products = JSON.parse(str);
                add();
            }
        };
        xmlhttp.open("GET", "./getCart.php");
        xmlhttp.send();
$('document').ready(function () {




});

function del(p1) {
    var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     // alert(this.responseText);
    }
  };
  xhttp.open("GET", './getCart.php?del='+p1, true);

  xhttp.send();


  
    
}
function add(){
    var element = "";
    for(i=0;i<products.length;i++){


        var id = Number(products[i][0]);
        var image = `<img class="d-inline-block" src="./images/products/${id}.png">`;
        var name = `<p>${products[i][1]}</p>`;
        var price = `<p>${products[i][2]} $</p>`;
        totalCost+= Number(products[i][2])

        element += `<span><div class="card text-secondary">
        <div class="card-body">${image}<div style="margin-left:10px" class="d-inline-block">
        ${name} ${price}`;
        element += `</div> </div><div class="card-footer">
        <button onclick='$(this).parents("span").hide();del(${id});totalCost-=${products[i][2]};total();' class="btn-danger btn">remove</button></div></div></span>`;

    }

    
    var items = document.getElementById('items');
    items.innerHTML += element;
    $('#total').text(totalCost +'$');
    $('#counter').text(products.length);


}
function total(){
    $('#total').text(totalCost +'$');
    
}
$(document).ready(function(){
  $("#buy").click(function(){
    for(var i=0; i<products.length;i++){
        var email = products[i][5];
        var userm = products[i][7];
            var body = "Product Name:" + products[i][1] +"<br>Price: "+ products[i][2] +"<br><br>" + products[i][6];
            var xmlhttmail = new XMLHttpRequest();
            xmlhttmail.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                //str += this.responseText;
                //products = JSON.parse(str);
                //add();
                
            }
        };
        xmlhttmail.open("GET", "https://kfupmharaj.000webhostapp.com/emails/PHPMailer/index.php?email="+email+"&body="+body+"&name="+userm , true);
        xmlhttmail.send();
        //alert(products.length)
        
    }
  }); 
});

function sendMails(){
    
        //alert(products.length)

}









