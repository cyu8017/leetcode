// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

export function maximumCount(nums: number[]): number {
    let pos = 0, neg = 0;
    for (const x of nums) {
        if (x > 0) pos++;
        else if (x < 0) neg++;
    }
    return Math.max(pos, neg);
}
