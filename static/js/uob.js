var items=[];
var asiamall;

function addtocart1(){
    var name = document.getElementById("name").innerHTML;
    var type= document.getElementById("type").innerHTML;
    var points = document.getElementById("points").innerHTML;
    var quantity = document.getElementById("Asia Mall $20 Gift Voucher").value;
    var totalpoints= points * quantity
    var asiamall= {"rewardname" : name,"type":type, "points":points,"quantity":quantity,"totalpoints":totalpoints};
    items.push(asiamall);
    console.log(items)

}
