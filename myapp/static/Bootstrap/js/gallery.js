var images = ["/static/images/sl1.jpg","/static/images/sl2.jpg","/static/images/sl3.jpg","/static/images/sl4.jpg"]
var num = 0;
function next() {

    var slider = document.getElementById("slider");

    num++;
    if(num>=images.length){
        num =0
    }

    slider.src = images[num]

    ;


}

function prev() {
    var slider = document.getElementById("slider");
    num--;
    if(num>=images.length){
        num =images.length -1
    }
    slider.src = images[num]
}

function close() {
    var slider = document.getElementById("slider");
    var t = setInterval(close,10);
    if (slider.height>0 && slider.width>0){

        slider.width=slider.width-1
    }
    else{
        clearInterval(t)
    }
function openq(){
         var slider = document.getElementById("slider");
    var t = setInterval(close,10);
    if (slider.height<700 && slider.width<1200){
        slider.height=slider.height+1;
        slider.width=slider.width+1
    }
    else{
        clearInterval(t)
    }

}

}



