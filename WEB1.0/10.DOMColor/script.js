function replace_font() {
    const h1 = document.querySelector('h1'); // Selects the h1 tag

    const font_input = document.querySelector('#font');
    let font_str = font_input.value;
    console.log(font_str);

    h1.style['font-family'] = font_str;
}

function replace_color() {
    // TODO: Complete this function to change the color of the h1 tag:
    // STEP 1: Get the h1 element as a variable using document.querySelector.
    const h1 = document.querySelector('h1');
    // STEP 2: Get the input element for "color" using document.querySelector.
    const color = document.querySelector('#color');
    // STEP 3: Get the value of the element using dot notation.
    const colorPicked = color.value;
    // At this point, it may be useful to print the color value to the console to make sure your code's working so far.
    // console.log(colorPicked);
    // STEP 4: Change the style of the h1 element to match the value from step 3. You can use `.style.color` to change the color.
    h1.style.color = colorPicked;
    h1.innerHTML = `Your favorite color is: ${colorPicked}`;
}

var randomColor = Math.floor(Math.random() * 16777215).toString(16);
const button = document.querySelector('#color');
const h1 = document.querySelector('h1');

button.addEventListener('keypress', () => {
    h1.style.color = get_random_color();
});

function get_random_color() {
    var color = '';
    for (var i = 0; i < 3; i++) {
        var sub = Math.floor(Math.random() * 256).toString(16);
        color += sub.length == 1 ? '0' + sub : sub;
    }
    return '#' + color;
}
