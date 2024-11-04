function toggleMobileMenu(menu) {
  menu.classList.toggle("open"); // Переключаем класс .open у #hamburger-icon

  if (menu.classList.contains("open")) {
    document.body.style.height = "100vh"; // Устанавливаем высоту body на 100vh
    document.body.style.overflow = "hidden"; // Отключаем прокрутку страницы
  } else {
    document.body.style.height = ""; // Возвращаем высоту body в исходное состояние
    document.body.style.overflow = ""; // Включаем прокрутку
  }
}
