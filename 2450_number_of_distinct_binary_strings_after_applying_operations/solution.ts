// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

export function countDistinctStrings(s: string, k: number): number {
    const mod = 1000000007;
    const n = s.length;
    let ans = 1;
    for (let i = 0; i < n - k + 1; i++) ans = (ans * 2) % mod;
    return ans;
}
