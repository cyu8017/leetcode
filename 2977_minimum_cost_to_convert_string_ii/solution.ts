// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

export function minimumCost(source: any, target: any, original: any, changed: any, cost: any): any {
    const INF = Number.MAX_SAFE_INTEGER / 4;
    const ids = new Map();
    for (let i = 0; i < original.length; i++) {
        if (!ids.has(original[i])) ids.set(original[i], ids.size);
        if (!ids.has(changed[i])) ids.set(changed[i], ids.size);
    }
    const m = ids.size;
    const dist = Array.from({length: m}, () => new Array(m).fill(INF));
    for (let i = 0; i < m; i++) dist[i][i] = 0;
    for (let i = 0; i < original.length; i++) {
        const u = ids.get(original[i]), v = ids.get(changed[i]);
        const ww = cost[i];
        if (ww < dist[u][v]) dist[u][v] = ww;
    }
    for (let k = 0; k < m; k++)
        for (let i = 0; i < m; i++)
            for (let j = 0; j < m; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
    const n = source.length;
    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;
    const lens = new Set();
    for (const key of ids.keys()) lens.add(key.length);
    for (let i = 0; i < n; i++) {
        if (dp[i] >= INF / 2) continue;
        if (source[i] === target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
        for (const L of lens) {
            if (i + L > n) continue;
            const ss = source.substring(i, i + L), tt = target.substring(i, i + L);
            if (!ids.has(ss) || !ids.has(tt)) continue;
            const iu = ids.get(ss), iv = ids.get(tt);
            if (dist[iu][iv] < INF / 2) {
                const cand = dp[i] + dist[iu][iv];
                if (cand < dp[i + L]) dp[i + L] = cand;
            }
        }
    }
    if (dp[n] >= INF / 2) return -1;
    return dp[n];
}
