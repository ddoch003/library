// User profile
let profileSubMenu = document.getElementById("profileSubMenu")
function toggleProfileMenu() {
    profileSubMenu.classList.toggle("profile-submenu-wrap-open-menu")
}

// Genres submenu
let genresSubMenu = document.getElementById("genresSubMenu");
let genresNavItem = document.getElementById("genresNavItem");

genresNavItem.addEventListener("mouseover", function () {
    genresSubMenu.classList.add("genres-submenu-wrap-open-menu");
})

genresNavItem.addEventListener("mouseout", function () {
    genresSubMenu.classList.remove("genres-submenu-wrap-open-menu");
})