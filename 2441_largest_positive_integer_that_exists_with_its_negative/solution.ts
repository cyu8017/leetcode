// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

export function findMaxK(nums: number[]): number {
    const seen = new Set();
    let ans = -1;
    for (const x of nums) {
        seen.add(x);
        if (x > 0 && seen.has(-x) && x > ans) ans = x;
        if (x < 0 && seen.has(-x) && -x > ans) ans = -x;
    }
    return ans;
}
