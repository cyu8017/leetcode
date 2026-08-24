// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

export function countEffectiveSubsequences(nums: any): any {
    const PopCount = (x) => {
        let c = 0;
        while (x !== 0) { c += x & 1; x >>= 1; }
        return c;
    };
    const mod = 1000000007;
    let all = 0;
    for (const x of nums) all |= x;
    const bits = [];
    for (let b = 0; b < 20; b++) if (((all >> b) & 1) !== 0) bits.push(b);
    const m = bits.length;
    const freq = new Array(1 << m).fill(0);
    for (const x of nums) {
        let mask = 0;
        for (let i = 0; i < m; i++) if (((x >> bits[i]) & 1) !== 0) mask |= 1 << i;
        freq[mask]++;
    }
    const disjoint = freq.slice();
    for (let b = 0; b < m; b++) {
        for (let mask = 0; mask < (1 << m); mask++) {
            if (((mask >> b) & 1) !== 0) disjoint[mask] += disjoint[mask ^ (1 << b)];
        }
    }
    const pow2 = new Array(nums.length + 1);
    pow2[0] = 1;
    for (let i = 1; i <= nums.length; i++) pow2[i] = pow2[i - 1] * 2 % mod;
    let ans = 0;
    const full = (1 << m) - 1;
    for (let s = 1; s <= full; s++) {
        const ways = pow2[disjoint[full ^ s]];
        const bc = PopCount(s);
        if ((bc & 1) !== 0) {
            ans += ways;
            if (ans >= mod) ans -= mod;
        } else {
            ans -= ways;
            if (ans < 0) ans += mod;
        }
    }
    return ans;
}
