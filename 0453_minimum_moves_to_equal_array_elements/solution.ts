// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

export class Solution {
    minMoves(nums: number[]): number {
        const minimum = Math.min(...nums);
        return nums.reduce((total, value) => total + value - minimum, 0);
    }
}
