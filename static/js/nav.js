/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function myFunction__nav() {
    document.getElementById("myDropdown__nav").classList.toggle("show");
}

function myFunction__nav__news() {
    document.getElementById("mySidenav").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.drop__btn')) {

    const dropdowns = document.getElementsByClassName("dropdown-content");
    let i;
    for (i = 0; i < dropdowns.length; i++) {
      const openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }

  if (!event.target.matches('.drop__btn__nav')) {

    const dropdowns__nav = document.getElementsByClassName("dropdown-content__nav");
    let i;
    for (i = 0; i < dropdowns__nav.length; i++) {
      const openDropdown__nav = dropdowns__nav[i];
      if (openDropdown__nav.classList.contains('show')) {
        openDropdown__nav.classList.remove('show');
      }
    }
  }

  if (!event.target.matches('.drop__btn__news')) {

    const dropdowns__news = document.getElementsByClassName("dropdown-content__news");
    let i;
    for (i = 0; i < dropdowns__news.length; i++) {
      const openDropdown__news = dropdowns__news[i];
      if (openDropdown__news.classList.contains('show')) {
        openDropdown__news.classList.remove('show');
      }
    }
  }
}
