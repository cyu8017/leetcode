// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution {
    findDuplicates(nums) {
        const result = [];
        for (const number of nums) {
            const index = Math.abs(number) - 1;
            if (nums[index] < 0) {
                result.push(Math.abs(number));
            } else {
                nums[index] = -nums[index];
            }
        }
        return result;
    }
}

module.exports = { Solution };
