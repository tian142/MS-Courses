import ctx, { size } from './mian.js';

ctx.restore();

const x = 4 * size;
const y = 4 * size;

ctx.fillStyle = 'purple';
ctx.fill();

ctx.beginPath();
ctx.arc(175, 175, 50, 0, Math.PI * 2, true); // Outer circle

ctx.arc(175, 175, 25, 0, Math.PI, false); // Mouth (clockwise)

ctx.arc(160, 155, 5, 0, Math.PI * 2, true); // Left eye

ctx.arc(190, 165, 15, 0, Math.PI * 2, true); // Right eye
