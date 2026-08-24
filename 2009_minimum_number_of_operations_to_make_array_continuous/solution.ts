// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

export function minOperations(nums: number[]): number {
    const n = nums.length;
    const uniq = [...new Set(nums)].sort((a, b) => a - b);
    let ans = n, j = 0;
    for (let i = 0; i < uniq.length; i++) {
        while (j < uniq.length && uniq[j] - uniq[i] + 1 <= n) j++;
        ans = Math.min(ans, n - (j - i));
    }
    return ans;
}
