"use strict";
function xorOperation(n, start) {
    let value = 0;
    for (let i = 0; i < n; i++)
        value ^= start + 2 * i;
    return value;
}
