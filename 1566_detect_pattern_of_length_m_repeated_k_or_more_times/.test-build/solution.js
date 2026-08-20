"use strict";
// LeetCode 1566 - Detect Pattern of Length M Repeated K or More Times
// https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
// @ts-nocheck
function containsPattern(arr, m, k) {
    let run = 0;
    for (let i = m; i < arr.length; i++) {
        run = arr[i] === arr[i - m] ? run + 1 : 0;
        if (run >= m * (k - 1))
            return true;
    }
    return false;
}
