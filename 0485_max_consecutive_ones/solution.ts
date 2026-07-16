// LeetCode 0485 - Max Consecutive Ones
// https://leetcode.com/problems/max-consecutive-ones/

export class Solution {
    findMaxConsecutiveOnes(nums: number[]): number {
        let best = 0;
        let current = 0;
        for (const num of nums) {
            if (num === 1) {
                current += 1;
                best = Math.max(best, current);
            } else {
                current = 0;
            }
        }
        return best;
    }
}
