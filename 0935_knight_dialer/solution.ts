// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

export function knightDialer(n: number): number {
    const MOD = 1000000007;
    const hops = [
        [4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9],
        [], [0, 1, 7], [2, 6], [1, 3], [2, 4]
    ];
    let dp = new Array(10).fill(1);
    for (let step = 1; step < n; step++) {
        const next = new Array(10).fill(0);
        for (let d = 0; d < 10; d++) {
            for (const to of hops[d]) next[to] = (next[to] + dp[d]) % MOD;
        }
        dp = next;
    }
    return dp.reduce((a, b) => (a + b) % MOD, 0);
}
