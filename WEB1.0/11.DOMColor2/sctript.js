// TODO: Add an event listener for each of the input elements on the page.

// STEP 1: Get the input element for "font" using document.querySelector, and save it to a const variable.

// STEP 2: Call the `.addEventListener()` method on that variable, and pass in the string 'input' as the first parameter, and the `replace_font` function as the second parameter.
// Make sure not to *call* replace_font - we are passing in the whole function, not calling it!!

// STEP 3: Repeat the above steps for the "color" input.

const font_input = document.querySelector('#font');
font_input.addEventListener('input', replace_font);
const color_input = document.querySelector('#color');
color_input.addEventListener('input', replace_color);

const bgc = document.querySelector('#bg');
bgc.addEventListener('input', () => {
  const bodyColor = document.queryselector('body');
  let inputColor = bgc.value;
  console.log(bgc.value);
  bodyColor.style.backgroundColor = inputColor;
});

function replace_font() {
  const h1 = document.querySelector('h1'); // Selects the h1 tag

  const font_input = document.querySelector('#font');
  let font_str = font_input.value;
  console.log(font_str);

  h1.style['font-family'] = font_str;
}

function replace_color() {
  const h1 = document.querySelector('h1'); // Selects the h1 tag

  const color_input = document.querySelector('#color');
  let color_str = color_input.value;
  console.log(color_str);

  h1.style.color = color_str;
  h1.innerHTML = `Your Favorite Color is: ${color_str}`;
}
