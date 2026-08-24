// LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

export function minimumChanges(s: string, k: number): number {
    const n = s.length;
    const INF = 1 << 20;
    const cost = Array.from({ length: n }, () => Array(n).fill(INF));
    const semiCost = (l, r) => {
        const length = r - l + 1;
        let best = INF;
        for (let d = 1; d < length; d++) {
            if (length % d !== 0) continue;
            let chg = 0;
            for (let start = 0; start < d; start++) {
                const chars = [];
                for (let i = l + start; i <= r; i += d) chars.push(s[i]);
                for (let i = 0, j = chars.length - 1; i < j; i++, j--)
                    if (chars[i] !== chars[j]) chg++;
            }
            if (chg < best) best = chg;
        }
        return best;
    };
    for (let i = 0; i < n; i++)
        for (let j = i + 1; j < n; j++)
            cost[i][j] = semiCost(i, j);
    const dp = Array.from({ length: k + 1 }, () => Array(n + 1).fill(INF));
    dp[0][0] = 0;
    for (let p = 1; p <= k; p++)
        for (let i = 1; i <= n; i++)
            for (let t = 0; t < i - 1; t++) {
                const cand = dp[p - 1][t] + cost[t][i - 1];
                if (cand < dp[p][i]) dp[p][i] = cand;
            }
    return dp[k][n];
}
