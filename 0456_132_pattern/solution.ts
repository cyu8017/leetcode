// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

export class Solution {
    find132pattern(nums: number[]): boolean {
        const stack: number[] = [];
        let third = Number.NEGATIVE_INFINITY;
        for (let i = nums.length - 1; i >= 0; i -= 1) {
            const value = nums[i];
            if (value < third) return true;
            while (stack.length && value > stack[stack.length - 1]) {
                third = stack.pop()!;
            }
            stack.push(value);
        }
        return false;
    }
}
