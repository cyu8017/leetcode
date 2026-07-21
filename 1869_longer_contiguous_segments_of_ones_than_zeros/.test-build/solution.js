"use strict";
// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
function checkZeroOnes(s) {
    let maxZeros = 0, maxOnes = 0, zeros = 0, ones = 0;
    for (const ch of s) {
        if (ch === "0") {
            zeros++;
            ones = 0;
            maxZeros = Math.max(maxZeros, zeros);
        }
        else {
            ones++;
            zeros = 0;
            maxOnes = Math.max(maxOnes, ones);
        }
    }
    return maxOnes > maxZeros;
}
