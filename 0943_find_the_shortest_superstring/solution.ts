// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

export function shortestSuperstring(words: string[]): string {
    const n = words.length;
    const overlap = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            const a = words[i], b = words[j];
            for (let k = Math.min(a.length, b.length); k > 0; k--) {
                if (a.slice(-k) === b.slice(0, k)) {
                    overlap[i][j] = k;
                    break;
                }
            }
        }
    }
    const N = 1 << n;
    const dp = Array.from({ length: N }, () => new Array(n).fill(null));
    for (let i = 0; i < n; i++) dp[1 << i][i] = words[i];
    for (let mask = 0; mask < N; mask++) {
        for (let last = 0; last < n; last++) {
            if ((mask & (1 << last)) === 0 || dp[mask][last] === null) continue;
            for (let nxt = 0; nxt < n; nxt++) {
                if ((mask & (1 << nxt)) !== 0) continue;
                const cand = dp[mask][last] + words[nxt].slice(overlap[last][nxt]);
                const nmask = mask | (1 << nxt);
                if (dp[nmask][nxt] === null || cand.length < dp[nmask][nxt].length)
                    dp[nmask][nxt] = cand;
            }
        }
    }
    const full = N - 1;
    let best = null;
    for (let i = 0; i < n; i++) {
        if (dp[full][i] !== null && (best === null || dp[full][i].length < best.length))
            best = dp[full][i];
    }
    return best;
}
