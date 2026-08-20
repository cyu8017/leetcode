"use strict";
function stringShift(s, shift) {
    let offset = 0;
    for (const [direction, amount] of shift)
        offset += direction === 0 ? -amount : amount;
    offset = ((offset % s.length) + s.length) % s.length;
    return s.slice(s.length - offset) + s.slice(0, s.length - offset);
}
