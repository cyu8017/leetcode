// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

/**
 * @param {number[]} nums
 * @return {number}
 */
var beautifulSubarrays = function(nums) {
    const freq = new Map([[0, 1]]);
    let xorv = 0, ans = 0;
    for (const x of nums) {
        xorv ^= x;
        ans += freq.get(xorv) || 0;
        freq.set(xorv, (freq.get(xorv) || 0) + 1);
    }
    return ans;
};
