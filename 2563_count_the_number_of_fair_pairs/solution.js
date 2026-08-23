// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var countFairPairs = function(nums, lower, upper) {
    nums.sort((a, b) => a - b);
    const count = (x) => {
        let ans = 0, l = 0, r = nums.length - 1;
        while (l < r) {
            if (nums[l] + nums[r] <= x) {
                ans += r - l;
                l++;
            } else r--;
        }
        return ans;
    };
    return count(upper) - count(lower - 1);
};
