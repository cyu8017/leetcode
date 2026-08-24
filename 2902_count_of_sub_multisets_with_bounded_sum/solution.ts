// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

export function countSubMultisets(nums: number[], l: number, r: number): number {
    const mod = 1000000007;
    const freq = new Map();
    let total = 0;
    for (const v of nums) {
        freq.set(v, (freq.get(v) || 0) + 1);
        total += v;
    }
    if (total < l) return 0;
    if (r > total) r = total;
    let dp = Array(r + 1).fill(0);
    dp[0] = 1;
    const zeros = freq.get(0) || 0;
    freq.delete(0);
    for (const [v, c] of freq) {
        const ndp = Array(r + 1).fill(0);
        for (let sum = 0; sum <= r; sum++) {
            if (dp[sum] === 0) continue;
            for (let k = 0; k <= c && sum + k * v <= r; k++)
                ndp[sum + k * v] = (ndp[sum + k * v] + dp[sum]) % mod;
        }
        dp = ndp;
    }
    let ans = 0;
    for (let s = l; s <= r; s++) ans = (ans + dp[s]) % mod;
    ans = Number((BigInt(ans) * BigInt(zeros + 1)) % BigInt(mod));
    return ans;
}
