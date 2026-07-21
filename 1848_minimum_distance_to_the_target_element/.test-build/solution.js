"use strict";
// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/
function getMinDistance(nums, target, start) {
    let best = nums.length;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target)
            best = Math.min(best, Math.abs(i - start));
    }
    return best;
}
