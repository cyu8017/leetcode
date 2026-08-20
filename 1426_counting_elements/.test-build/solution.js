"use strict";
function countElements(arr) {
    const values = new Set(arr);
    return arr.reduce((count, x) => count + values.has(x + 1), 0);
}
