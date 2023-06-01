// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
// 	container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

// add event listener to "Sign Up" button
signUpButton.addEventListener('click', () => {
   container.classList.add("right-panel-active");
});

// add event listener to "Sign In" button
signInButton.addEventListener('click', () => {
   container.classList.remove("right-panel-active");
});

// validate sign up form
const signUpForm = document.getElementById('signup-form');
signUpForm.addEventListener('submit', (e) => {
   // prevent default form submission behavior
   e.preventDefault();

   // send AJAX request to Django server to handle form submission
   const xhr = new XMLHttpRequest();
   xhr.open('POST', signUpForm.action);
   xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
   xhr.setRequestHeader('X-CSRFToken', csrf_token);
   xhr.onload = function() {
      if (xhr.status === 200) {
         // redirect to home page or display success message
         window.location.href = "{% url 'home' %}";
      } else {
         // display error message
         console.error(xhr.responseText);
      }
   };
   xhr.send(new FormData(signUpForm));
});

// validate sign in form
const signInForm = document.getElementById('signin-form');
signInForm.addEventListener('submit', (e) => {
   // prevent default form submission behavior
   e.preventDefault();

   // send AJAX request to Django server to handle form submission
   const xhr = new XMLHttpRequest();
   xhr.open('POST', signInForm.action);
   xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
   xhr.setRequestHeader('X-CSRFToken', csrf_token);
   xhr.onload = function() {
      if (xhr.status === 200) {
         // redirect to home page or display success message
         window.location.href = "{% url 'home' %}";
      } else {
         // display error message
         console.error(xhr.responseText);
      }
   };
   xhr.send(new FormData(signInForm));
});

