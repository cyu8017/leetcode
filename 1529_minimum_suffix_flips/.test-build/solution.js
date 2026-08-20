"use strict";
// LeetCode 1529 - Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/
// @ts-nocheck
function minFlips(target) {
    let ans = 0;
    let prev = "0";
    for (const ch of target) {
        if (ch !== prev) {
            ans++;
            prev = ch;
        }
    }
    return ans;
}
