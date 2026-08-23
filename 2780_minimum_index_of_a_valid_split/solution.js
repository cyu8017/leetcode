// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumIndex = function(nums) {
    const freq = new Map();
    let dom = 0, best = 0;
    for (const v of nums) {
        const c = (freq.get(v) || 0) + 1;
        freq.set(v, c);
        if (c > best) { best = c; dom = v; }
    }
    let left = 0;
    const n = nums.length;
    for (let i = 0; i < n - 1; i++) {
        if (nums[i] === dom) left++;
        const right = best - left;
        if (left * 2 > i + 1 && right * 2 > n - i - 1) return i;
    }
    return -1;
};
