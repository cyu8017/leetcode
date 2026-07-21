"use strict";
// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/
function maxFrequency(nums, k) {
    nums = [...nums].sort((a, b) => a - b);
    let left = 0;
    let windowSum = 0;
    let best = 0;
    for (let right = 0; right < nums.length; right++) {
        const value = nums[right];
        windowSum += value;
        while (value * (right - left + 1) - windowSum > k) {
            windowSum -= nums[left];
            left += 1;
        }
        best = Math.max(best, right - left + 1);
    }
    return best;
}
