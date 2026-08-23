// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestNiceSubarray = function(nums) {
    let used = 0, left = 0, ans = 0;
    for (let right = 0; right < nums.length; right++) {
        while ((used & nums[right]) !== 0) {
            used ^= nums[left];
            left++;
        }
        used |= nums[right];
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
};
