// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

/**
 * @param {number[]} nums
 * @param {number} value
 * @return {number}
 */
var findSmallestInteger = function(nums, value) {
    const cnt = new Array(value).fill(0);
    for (let x of nums) {
        let r = x % value;
        if (r < 0) r += value;
        cnt[r]++;
    }
    let mex = 0;
    while (cnt[mex % value] > 0) {
        cnt[mex % value]--;
        mex++;
    }
    return mex;
};
