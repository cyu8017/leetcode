"use strict";
// LeetCode 1550 - Three Consecutive Odds
// https://leetcode.com/problems/three-consecutive-odds/
// @ts-nocheck
function threeConsecutiveOdds(arr) {
    let run = 0;
    for (const value of arr) {
        run = value & 1 ? run + 1 : 0;
        if (run === 3)
            return true;
    }
    return false;
}
