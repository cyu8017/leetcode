// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

export function countKDifference(nums: number[], k: number): number {
    const freq = new Map();
    let ans = 0;
    for (const x of nums) {
        ans += freq.get(x - k) || 0;
        ans += freq.get(x + k) || 0;
        freq.set(x, (freq.get(x) || 0) + 1);
    }
    return ans;
}
