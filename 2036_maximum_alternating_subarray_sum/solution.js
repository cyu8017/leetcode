// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumAlternatingSubarraySum = function(nums) {
    let ans = Number.MIN_SAFE_INTEGER, even = 0, odd = 0;
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        if (i % 2 === 0) even += x;
        else even = Math.max(0, even - x);
        ans = Math.max(ans, even);
    }
    odd = 0;
    for (let i = 1; i < nums.length; i++) {
        const x = nums[i];
        if (i % 2 === 1) odd += x;
        else odd = Math.max(0, odd - x);
        ans = Math.max(ans, odd);
    }
    return ans;
};
