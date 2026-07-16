// LeetCode 0137 - Single Number II
// https://leetcode.com/problems/single-number-ii/

export function singleNumber(nums: number[]): number {
    let ones = 0;
    let twos = 0;

    for (const num of nums) {
        ones = (ones ^ num) & ~twos;
        twos = (twos ^ num) & ~ones;
    }

    return ones;
}