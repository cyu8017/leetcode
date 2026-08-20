// LeetCode 1994 - The Number of Good Subsets
// https://leetcode.com/problems/the-number-of-good-subsets/

function numberOfGoodSubsets(nums: number[]): number {
    const MOD = 1000000007n;
    const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
    const masks = new Array(31).fill(0);
    for (let x = 2; x <= 30; x++) {
        let m = 0, y = x, ok = true;
        for (let i = 0; i < primes.length; i++) {
            const p = primes[i];
            if (y % p === 0) {
                if (Math.floor(y / p) % p === 0) {
                    ok = false;
                    break;
                }
                m |= 1 << i;
                y = Math.floor(y / p);
            }
        }
        masks[x] = ok ? m : -1;
    }
    const cnt = new Array(31).fill(0);
    for (const v of nums) cnt[v]++;
    const dp = new Array(1 << primes.length).fill(0n);
    dp[0] = 1n;
    for (let x = 2; x <= 30; x++) {
        if (cnt[x] === 0 || masks[x] < 0) continue;
        const m = masks[x];
        for (let state = (1 << primes.length) - 1; state >= 0; state--) {
            if (state & m) continue;
            dp[state | m] = (dp[state | m] + dp[state] * BigInt(cnt[x])) % MOD;
        }
    }
    let ans = 0n;
    for (let i = 1; i < dp.length; i++) ans = (ans + dp[i]) % MOD;
    let mul = 1n;
    for (let i = 0; i < cnt[1]; i++) mul = mul * 2n % MOD;
    return Number(ans * mul % MOD);
}
