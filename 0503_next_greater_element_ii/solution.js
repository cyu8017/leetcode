// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

class Solution {
    nextGreaterElements(nums) {
        const length = nums.length;
        const result = Array(length).fill(-1);
        const stack = [];
        for (let index = 0; index < length * 2; index += 1) {
            while (stack.length && nums[stack[stack.length - 1]] < nums[index % length]) {
                result[stack.pop()] = nums[index % length];
            }
            if (index < length) stack.push(index);
        }
        return result;
    }
}

module.exports = { Solution };
