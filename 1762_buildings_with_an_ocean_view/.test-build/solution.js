"use strict";
// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/
function findBuildings(heights) {
    const ans = [];
    let tallest = 0;
    for (let i = heights.length - 1; i >= 0; i--) {
        if (heights[i] > tallest) {
            ans.push(i);
            tallest = heights[i];
        }
    }
    return ans.reverse();
}
