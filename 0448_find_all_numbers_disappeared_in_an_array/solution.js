// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution {
    findDisappearedNumbers(nums) {
        for (const number of nums) {
            const index = Math.abs(number) - 1;
            if (nums[index] > 0) {
                nums[index] = -nums[index];
            }
        }
        const result = [];
        for (let index = 0; index < nums.length; index += 1) {
            if (nums[index] > 0) {
                result.push(index + 1);
            }
        }
        return result;
    }
}

module.exports = { Solution };
