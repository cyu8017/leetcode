// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

export class Solution {
    findPermutation(s: string): number[] {
        const stack = [1];
        const result: number[] = [];
        for (const ch of s) {
            if (ch === "I") {
                while (stack.length) result.push(stack.pop() as number);
            }
            stack.push(stack.length + result.length + 1);
        }
        while (stack.length) result.push(stack.pop() as number);
        return result;
    }
}
