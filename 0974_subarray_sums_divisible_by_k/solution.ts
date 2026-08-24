// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

export function subarraysDivByK(nums: number[], k: number): number {
    const count = new Map([[0, 1]]);
    let prefix = 0, ans = 0;
    for (const x of nums) {
        prefix = ((prefix + x) % k + k) % k;
        ans += count.get(prefix) || 0;
        count.set(prefix, (count.get(prefix) || 0) + 1);
    }
    return ans;
}
