// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

export function maxSubsequence(nums: number[], k: number): number[] {
    const n = nums.length;
    const arr = Array.from({length: n}, (_, i) => [nums[i], i]);
    arr.sort((a, b) => b[0] - a[0]);
    const idx = arr.slice(0, k).map(x => x[1]).sort((a, b) => a - b);
    return idx.map(i => nums[i]);
}
