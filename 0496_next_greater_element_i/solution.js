// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

class Solution {
    nextGreaterElement(nums1, nums2) {
        const nextGreater = new Map();
        const stack = [];
        for (const num of nums2) {
            while (stack.length && stack[stack.length - 1] < num) {
                nextGreater.set(stack.pop(), num);
            }
            stack.push(num);
        }
        return nums1.map((num) => nextGreater.get(num) ?? -1);
    }
}

module.exports = { Solution };
