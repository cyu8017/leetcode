// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

export class Solution {
    nextGreaterElement(nums1: number[], nums2: number[]): number[] {
        const nextGreater = new Map<number, number>();
        const stack: number[] = [];
        for (const num of nums2) {
            while (stack.length && stack[stack.length - 1] < num) {
                nextGreater.set(stack.pop() as number, num);
            }
            stack.push(num);
        }
        return nums1.map((num) => nextGreater.get(num) ?? -1);
    }
}
