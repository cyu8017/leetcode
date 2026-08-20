"use strict";
// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
// @ts-nocheck
function getLastMoment(n, left, right) {
    const leftMax = left.length ? Math.max(...left) : 0;
    const rightMin = right.length ? Math.min(...right) : n;
    return Math.max(leftMax, n - rightMin);
}
