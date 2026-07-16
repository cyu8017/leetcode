// LeetCode 0136 - Single Number
// https://leetcode.com/problems/single-number/

export function singleNumber(nums: number[]): number {
    let result = 0;
    for (const num of nums) {
        result ^= num;
    }
    return result;
}