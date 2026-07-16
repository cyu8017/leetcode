// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumSmaller = function(nums, target) {
    nums.sort((a, b) => a - b);
    let count = 0;
    for (let index = 0; index < nums.length - 2; index++) {
        let left = index + 1;
        let right = nums.length - 1;
        while (left < right) {
            const total = nums[index] + nums[left] + nums[right];
            if (total < target) {
                count += right - left;
                left += 1;
            } else {
                right -= 1;
            }
        }
    }
    return count;
};
