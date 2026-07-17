"use strict";
// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
function maximumScore(nums, multipliers) {
    const n = nums.length;
    const m = multipliers.length;
    let next = new Array(m + 1).fill(0);
    for (let i = m - 1; i >= 0; i--) {
        const cur = new Array(m + 1).fill(0);
        for (let left = i; left >= 0; left--) {
            const right = n - 1 - (i - left);
            const takeLeft = nums[left] * multipliers[i] + next[left + 1];
            const takeRight = nums[right] * multipliers[i] + next[left];
            cur[left] = Math.max(takeLeft, takeRight);
        }
        next = cur;
    }
    return next[0];
}
