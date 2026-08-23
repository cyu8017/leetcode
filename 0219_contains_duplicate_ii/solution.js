// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const lastIndex = new Map();
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (lastIndex.has(num) && i - lastIndex.get(num) <= k) {
            return true;
        }
        lastIndex.set(num, i);
    }
    return false;
};
