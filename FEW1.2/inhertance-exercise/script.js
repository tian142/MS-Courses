// Canvas and context
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

// This Class draws a rectange on a canvas
class Sprite {
  constructor(x, y, width, height, color = 'red') {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.color = color;
    this.rotate = 20;
  }

  moveTo(x, y) {
    this.x = x;
    this.y = y;
  }

  render(ctx) {
    ctx.save();

    ctx.translate(this.x, this.y);
    ctx.rotate((this.rotate * Math.PI) / 180);
    ctx.beginPath();
    ctx.fillStyle = this.color;
    ctx.fillRect(-this.width / 2, -this.height / 2, this.width, this.height);
    ctx.fill();
    ctx.restore();
  }
}

// Make a Sprite
const box = new Sprite(0, 0, 40, 40, 'purple');

box.moveTo(180, 180); // Move the sprite
box.render(ctx); // render the sprite
// box.rotate(ctx);

// * Challenge: Make another sprite
const box2 = new Sprite(0, 0, 40, 40, 'fuchsia');
box.moveTo(10, 10); // Move the sprite
box2.render(ctx); // render the sprite

// * Challenge: Make a few more sprites, position, and
// render them. Stetch goal use a loop to many
for (let i = 0; i < 100; i += 1) {
  const x = Math.random() * 400;
  const y = Math.random() * 400;
  const s = new Sprite(x, y, 8, 16, 'pink');
  s.render(ctx);
}

const box4 = new Sprite(40, 50, 40, 40, 'green');
box4.render(ctx); // render the sprite

// * Challenge: Make a Circle class it should

class Circle extends Sprite {
  constructor(x, y, radius, color = 'red') {
    super(x, y, radius * 2, radius * 2, color);
    this.radius = radius;
  }

  render(ctx) {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.fill();
    ctx.closePath();
  }
}

// Make an instance of Circle
// Call moveTo(x, y) on your circle
// render the circle
const circle1 = new Circle(200, 60, 20, 'red');
circle1.render(ctx);

// * Challenge: Make a few circle of different sizes
// and colors. Position the new circles by calling
// their moveTo(x, y) method. Stretch goal use a loop!
const circle2 = new Circle(200, 300, 40, '#4287f5');
circle2.render(ctx);

for (let i = 0; i < 50; i += 1) {
  const x = Math.random() * 400;
  const y = Math.random() * 400;
  const s = new Circle(x, y, 8, 'lavender');
  s.render(ctx);
}

// * Challenge: Below is a Label class that draws text
// on a canvas. It extends Sprite.
// Add a font property to set the font style of
// the text.

class Label extends Sprite {
  constructor(x, y, text, color) {
    super(x, y, undefined, undefined, color);
    this.text = text;
  }

  render(ctx) {
    ctx.save();
    ctx.rotate((this.rotate * Math.PI) / 180);
    ctx.translate(this.x / 2, this.y / 2);
    ctx.beginPath();
    ctx.font = '30px Helvetica';
    ctx.fillStyle = this.color;
    ctx.fillText(this.text, this.x, this.y);
    ctx.restore();
  }
}

const t = new Label(120, 50, 'Hello World', 'black');
t.text = 'Foo Bar';
t.moveTo(200, 44);
t.render(ctx);

// * Challenge: It would be great if there were a
// rotate property.
// To rotate a drawing on the canvas you need to:

// save the canvas context: ctx.save()
// rotate the canvas: ctx.rotate(radians)
// draw your paths...
// fill your shapes...
// restore the canvas: ctx.restore()

// Add a rotate property to Sprite.
// It can have a default value of 0.
// Add the rotation code to Sprite's render()
// method.

// Now rotate set the rotate property on your
// object before rendering them. Something like:
// box.rotate = Math.PI / 4 (should be 45deg)
// box.render(ctx)

// * Challenge: It would be nice if you could chain
// method calls on your class. For example:

// box.moveTo(1, 5).render(ctx)

// You can make this happen by returning this from
// all methods in your class. Since the Sprite
// class is the super class and is extended by the
// Circle, Label, and Polygon class making changes
// there will apply to these sub classes.

// Add: return this to the render() and moveTo()
// methods in Sprite.

// * Challenge: Below is a polygon class. It extends
// sprite.

/*
class Polygon extends Sprite {
  constructor(x, y, radius, sides, color) {
    super(x, y, radius * 2, radius * 2, color)
    this.radius = radius
    this.sides = sides
  }

  render(ctx) {
    ctx.beginPath()
    ctx.fillStyle = this.color

    ctx.moveTo(Math.cos(0) * this.radius + this.x, Math.sin(0) * 
    this.radius + this.y)

    const step = Math.PI * 2 / this.sides

    for (let i = 0; i < this.sides; i += 1) {
      const x = Math.cos(i * step) * this.radius + this.x
      const y = Math.sin(i * step) * this.radius + this.y
      ctx.lineTo(x, y)
    }
    ctx.fill()
  }
}

const p = new Polygon(100, 100, 40, 6)
p.render(ctx)
*/

// What if there was a class that managed an array of shapes?
//
