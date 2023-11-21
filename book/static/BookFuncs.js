function DeleteBook(id) {
  const token = getCookie("csrftoken");
  // Create an XMLHttpRequest object
  const xhttp = new XMLHttpRequest();

  // Define a callback function
  xhttp.onload = function () {
    window.location.reload();
  };

  // Send a request
  xhttp.open("DELETE", "/books/" + id + "/delete");
  xhttp.setRequestHeader("X-CSRFToken", token);
  xhttp.send();
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}
