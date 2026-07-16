// LeetCode 0189 - Rotate Array
// https://leetcode.com/problems/rotate-array/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void}
 */
var rotate = function(nums, k) {
    const reverse = (left, right) => {
        while (left < right) {
            [nums[left], nums[right]] = [nums[right], nums[left]];
            left++;
            right--;
        }
    };

    k %= nums.length;
    reverse(0, nums.length - 1);
    reverse(0, k - 1);
    reverse(k, nums.length - 1);
};