window.onload = function() {
  var tabsHeader = document.querySelector(".tabs-header"),
    tabH = document.getElementsByClassName("tab-h"),
    tabBody = document.getElementsByClassName("tab-b");
    tabsHeader.addEventListener("click", fTabs);
  function fTabs(event) {
    if (event.target.className == "tab-h") {
      var dataTab = event.target.getAttribute("data-tab");

      // Перебираем массив
      for (var i = 0; i < tabBody.length; i++) {

        if (dataTab == i) {

          tabBody[i].style.opacity = "1";
          tabBody[i].style.top = "34px";

          event.target.style.color = "black";
          event.target.style.backgroundColor = "#f0f0f0";
        } else {
          tabBody[i].style.opacity = "0";
          tabBody[i].style.top = "80px";

          for (var h = 0; h < tabH.length; h++) {

            if (tabH[h].getAttribute("data-tab") != dataTab) {
              tabH[h].style.color = "#f0f0f0";
              tabH[h].style.backgroundColor = "#5c6169";
            }
          }
        }
      }
    }
  }
};
document.getElementById('nav').onmouseover = function(event){

	var target = event.target;
	if(target.className == 'menu-item'){
		var s = target.getElementsByClassName('submenu');
		closeMenu();
		s[0].style.display = 'block';
	}
};

document.onmouseover = function(event){
	var target = event.target;
	console.log(event.target);
	if(target.className != 'menu-item' && target.className != 'submenu'){
		closeMenu();
	}
};

function closeMenu(){
	// var menu = document.getElementById('nav');   - ненужная строка. нигде не участвует!
	var subm = document.getElementsByClassName('submenu');
	for(var i = 0; i < subm.length; i++){
		subm[i].style.display = "none";
	}
}



