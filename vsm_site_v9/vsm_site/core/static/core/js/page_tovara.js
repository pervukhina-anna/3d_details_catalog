// Здесь можно добавить скрипты для дополнительной функциональности, если необходимо
document.getElementById("addToCart").addEventListener("click", function() {
    // При нажатии на кнопку "Добавить в корзину"
    // Показываем уведомление
    document.getElementById("notification").style.display = "block";
  
    // Через 3 секунды скрываем уведомление
    setTimeout(function() {
      document.getElementById("notification").style.display = "none";
    }, 3000);
  });
  
  function showImage(imagePath) {
    // Заменяем изображение в блоке "selected-image"
    document.querySelector(".selected-image img").src = imagePath;
  }
  