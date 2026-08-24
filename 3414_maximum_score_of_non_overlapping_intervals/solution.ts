// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

export function maximumWeight(intervals: any): any {
    const n = intervals.length;
    const arr = intervals.map((it, i) => ({ l: it[0], r: it[1], w: it[2], i }));
    arr.sort((a, b) => a.r - b.r);
    const copyState = (s) => ({ score: s.score, idx: s.idx.slice() });
    const better = (a, b) => {
        if (a.score !== b.score) return a.score > b.score ? a : b;
        const m = Math.min(a.idx.length, b.idx.length);
        for (let i = 0; i < m; i++) {
            if (a.idx[i] !== b.idx[i]) return a.idx[i] < b.idx[i] ? a : b;
        }
        return a.idx.length <= b.idx.length ? a : b;
    };
    const dp = Array.from({ length: n + 1 }, () =>
        Array.from({ length: 5 }, () => ({ score: 0, idx: [] }))
    );
    for (let i = 1; i <= n; i++) {
        const cur = arr[i - 1];
        for (let t = 0; t <= 4; t++) dp[i][t] = copyState(dp[i - 1][t]);
        let lo = 0, hi = i - 1;
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (arr[mid].r < cur.l) lo = mid + 1;
            else hi = mid;
        }
        const prev = lo;
        for (let t = 1; t <= 4; t++) {
            const prevState = dp[prev][t - 1];
            const cand = copyState(prevState);
            cand.score = prevState.score + cur.w;
            cand.idx.push(cur.i);
            cand.idx.sort((a, b) => a - b);
            dp[i][t] = better(dp[i][t], cand);
        }
    }
    let best = dp[n][0];
    for (let t = 1; t <= 4; t++) best = better(best, dp[n][t]);
    return best.idx;
}
