// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countAlternatingSubarrays = function(nums) {
    let ans = 1, s = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[i - 1]) s++;
        else s = 1;
        ans += s;
    }
    return ans;
};
