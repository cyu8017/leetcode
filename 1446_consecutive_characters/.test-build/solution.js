"use strict";
function maxPower(s) { let best = 0, run = 0, previous = ""; for (const ch of s) {
    run = ch === previous ? run + 1 : 1;
    previous = ch;
    best = Math.max(best, run);
} return best; }
