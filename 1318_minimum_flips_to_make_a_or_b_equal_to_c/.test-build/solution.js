"use strict";
// LeetCode 1318 - Minimum Flips To Make A Or B Equal To C
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
function minFlips(a, b, c) {
    let flips = 0;
    while (a || b || c) {
        const x = a & 1, y = b & 1, z = c & 1;
        flips += z === 0 ? x + y : (x === 0 && y === 0 ? 1 : 0);
        a >>= 1;
        b >>= 1;
        c >>= 1;
    }
    return flips;
}
