// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

export function minImpossibleOR(nums: number[]): number {
    const set = new Set(nums);
    let x = 1;
    while (set.has(x)) x <<= 1;
    return x;
}
