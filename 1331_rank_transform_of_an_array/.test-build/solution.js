"use strict";
// LeetCode 1331 - Rank Transform Of An Array
// https://leetcode.com/problems/rank-transform-of-an-array/
function arrayRankTransform(arr) {
    const sorted = [...new Set(arr)].sort((a, b) => a - b);
    const rank = new Map(sorted.map((value, i) => [value, i + 1]));
    return arr.map((value) => rank.get(value));
}
