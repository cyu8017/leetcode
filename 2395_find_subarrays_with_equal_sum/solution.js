// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var findSubarrays = function(nums) {
    const seen = new Set();
    for (let i = 0; i + 1 < nums.length; i++) {
        const s = nums[i] + nums[i + 1];
        if (seen.has(s)) return true;
        seen.add(s);
    }
    return false;
};
