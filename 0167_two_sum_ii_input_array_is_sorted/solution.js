// LeetCode 0167 - Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

/**
 * Returns 1-indexed positions of two values summing to target.
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let left = 0;
    let right = numbers.length - 1;

    while (left < right) {
        const total = numbers[left] + numbers[right];
        if (total === target) {
            return [left + 1, right + 1];
        }
        if (total < target) {
            left++;
        } else {
            right--;
        }
    }
    return [];
};