// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let mx = nums[0];
    for (const x of nums) if (x > mx) mx = x;
    let ans = 0, cur = 0;
    for (const x of nums) {
        if (x === mx) {
            cur++;
            ans = Math.max(ans, cur);
        } else cur = 0;
    }
    return ans;
};
