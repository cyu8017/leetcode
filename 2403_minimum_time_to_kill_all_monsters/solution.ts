// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

export function minimumTime(power: number[]): number {
    const bitCount = (x) => {
        let c = 0;
        while (x !== 0) { c += x & 1; x >>= 1; }
        return c;
    };
    const n = power.length;
    const N = 1 << n;
    const dp = Array(N).fill(Number.MAX_SAFE_INTEGER / 4);
    dp[0] = 0;
    for (let mask = 0; mask < N; mask++) {
        const killed = bitCount(mask);
        const gain = killed + 1;
        for (let i = 0; i < n; i++) {
            if ((mask & (1 << i)) !== 0) continue;
            const need = Math.floor((power[i] + gain - 1) / gain);
            const nm = mask | (1 << i);
            dp[nm] = Math.min(dp[nm], dp[mask] + need);
        }
    }
    return dp[N - 1];
}
