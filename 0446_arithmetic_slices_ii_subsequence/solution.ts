// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

export class Solution {
    numberOfArithmeticSlices(nums: number[]): number {
        let total = 0;
        const differences: Map<number, number>[] = nums.map(() => new Map());

        for (let index = 0; index < nums.length; index += 1) {
            const value = nums[index];
            for (let previous = 0; previous < index; previous += 1) {
                const diff = value - nums[previous];
                total += differences[previous].get(diff) ?? 0;
                differences[index].set(
                    diff,
                    (differences[index].get(diff) ?? 0) + (differences[previous].get(diff) ?? 0) + 1,
                );
            }
        }

        return total;
    }
}
