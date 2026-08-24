// LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

var maxSubarrayLength = function(nums, k) {
    const freq = new Map();
    let ans = 0, left = 0;
    for (let right = 0; right < nums.length; right++) {
        freq.set(nums[right], (freq.get(nums[right]) || 0) + 1);
        while (freq.get(nums[right]) > k) {
            freq.set(nums[left], freq.get(nums[left]) - 1);
            left++;
        }
        if (right - left + 1 > ans) ans = right - left + 1;
    }
    return ans;
};
