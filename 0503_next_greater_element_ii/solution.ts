// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

export class Solution {
    nextGreaterElements(nums: number[]): number[] {
        const length = nums.length;
        const result = Array<number>(length).fill(-1);
        const stack: number[] = [];
        for (let index = 0; index < length * 2; index += 1) {
            while (stack.length && nums[stack[stack.length - 1]] < nums[index % length]) {
                result[stack.pop() as number] = nums[index % length];
            }
            if (index < length) stack.push(index);
        }
        return result;
    }
}
