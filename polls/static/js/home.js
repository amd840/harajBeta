var allproducts = [[[1,1,0],[1,2,0],[1,3,0],[1,4,0],[1,5,0]],[[2,1,0],[2,2,0]]];

$('document').ready(function () {

	
    var therows  = '';   
   	for(i=0;i<allproducts.length;i++){
   		items = '';
   		for(j=0;j<allproducts[i].length;j++){
   			var tempitem = `<div class="item">
                        <div class="card pad15">
                            <div class="card-header pad15">${allproducts[i][j][1]}</div>
                            <div class="card-body"><img src="./images/cart.png"></div>
                            <div class=" card-footer">
                                <label >Prise</label> <label>00.00$</label>
                                <button class="btn-info float-right ">add to card</button>
                            </div>
                        </div>
                       </div>`;
   			items+=(tempitem);
   		}
   		//alert(items)
   		var tempRow = `
   		<div class="row">
        <div class="MultiCarousel" data-items="1,3,5,6" data-slide="1" id="MultiCarousel${i}"  data-interval="1000">
            <p class="alert alert-dark">The Most Sell</p>
            <div class="MultiCarousel-inner">
            ${items}

   		</div>
            <button class="btn btn-primary leftLst"><</button>
            <button class="btn btn-primary rightLst">></button>
        </div>
        </div>`;

   		therows+=(tempRow);
   		

    }
    //alert(therows);
    var main = $('.container').empty();
    main.append(therows);




});

/*<div class="container">

    <div class="row">
        <div class="MultiCarousel" data-items="1,3,5,6" data-slide="1" id="MultiCarousel"  data-interval="1000">
            <p class="alert alert-dark">The Most Sell</p>
            <div class="MultiCarousel-inner">


                <div class="item">
                        <div class="card pad15">
                            <div class="card-header pad15">Item</div>
                            <div class="card-body"><img src="images/cart.png"></div>
                            <div class=" card-footer">
                                <label >Prise</label> <label>00.00$</label>
                                <button class="btn-info float-right ">add to card</button>
                            </div>
                        </div>
                </div>
                <div class="item">
                    <div class="card pad15">
                        <div class="card-header pad15">Item1</div>
                        <div class="card-body"><img src="images/cart.png"></div>
                        <div class=" card-footer">
                            <label >Prise</label> <label>00.00$</label>
                            <button class="btn-info float-right ">add to card</button>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <div class="card pad15">
                        <div class="card-header pad15">Item2</div>
                        <div class="card-body"><img src="images/cart.png"></div>
                        <div class=" card-footer">
                            <label >Prise</label> <label>00.00$</label>
                            <button class="btn-info float-right ">add to card</button>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <div class="card pad15">
                        <div class="card-header pad15">Item3</div>
                        <div class="card-body"><img src="images/cart.png"></div>
                        <div class=" card-footer">
                            <label >Prise</label> <label>00.00$</label>
                            <button class="btn-info float-right ">add to card</button>
                        </div>
                    </div>
                </div>




            </div>
            <button class="btn btn-primary leftLst"><</button>
            <button class="btn btn-primary rightLst">></button>
        </div>
    </div>
    <div class="row">
        <div class="MultiCarousel" data-items="1,3,5,6" data-slide="1" id="MultiCarousel2"  data-interval="1000">
            <p class="alert alert-dark">Seller #1</p>
            <div class="MultiCarousel-inner">


                <div class="item">
                    <div class="card pad15">
                        <div class="card-header pad15">Item</div>
                        <div class="card-body"><img src="images/cart.png"></div>
                        <div class=" card-footer">
                            <label >Prise</label> <label>00.00$</label>
                            <button class="btn-info float-right ">add to card</button>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <div class="card pad15">
                        <div class="card-header pad15">Item1</div>
                        <div class="card-body"><img src="images/cart.png"></div>
                        <div class=" card-footer">
                            <label >Prise</label> <label>00.00$</label>
                            <button class="btn-info float-right ">add to card</button>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <div class="card pad15">
                        <div class="card-header pad15">Item2</div>
                        <div class="card-body"><img src="images/cart.png"></div>
                        <div class=" card-footer">
                            <label >Prise</label> <label>00.00$</label>
                            <button class="btn-info float-right ">add to card</button>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <div class="card pad15">
                        <div class="card-header pad15">Item3</div>
                        <div class="card-body"><img src="images/cart.png"></div>
                        <div class=" card-footer">
                            <label >Prise</label> <label>00.00$</label>
                            <button class="btn-info float-right ">add to card</button>
                        </div>
                    </div>
                </div>




            </div>
            <button class="btn btn-primary leftLst"><</button>
            <button class="btn btn-primary rightLst">></button>
        </div>
    </div>

</div>*/