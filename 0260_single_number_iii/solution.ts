// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

export function singleNumber(nums: number[]): number[] {
    let xorAll = 0;
    for (const num of nums) {
        xorAll ^= num;
    }
    const diff = xorAll & -xorAll;
    let first = 0;
    let second = 0;
    for (const num of nums) {
        if (num & diff) {
            first ^= num;
        } else {
            second ^= num;
        }
    }
    return [first, second];
}
