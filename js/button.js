// Resources:
// * [Document.createElement() - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
// * [Node.appendChild() - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)
// * [When to use the Button Element - CSS Tricks](https://css-tricks.com/use-button-element/)

// 1. Create the button
var button = document.createElement("button");
button.innerHTML = "Do Something";

// 2. Append somewhere
var body = document.getElementsByTagName("body")[0];
body.appendChild(button);

// 3. Add event handler
button.addEventListener ("click", function() {
  alert("did something");
});