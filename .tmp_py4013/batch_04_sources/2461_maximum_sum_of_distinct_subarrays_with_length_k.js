// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumSubarraySum = function(nums, k) {
    const cnt = new Map();
    let sum = 0, ans = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        cnt.set(nums[i], (cnt.get(nums[i]) || 0) + 1);
        if (i >= k) {
            const y = nums[i - k];
            sum -= y;
            const c = cnt.get(y) - 1;
            if (c === 0) cnt.delete(y);
            else cnt.set(y, c);
        }
        if (i >= k - 1 && cnt.size === k && sum > ans) ans = sum;
    }
    return ans;
};
