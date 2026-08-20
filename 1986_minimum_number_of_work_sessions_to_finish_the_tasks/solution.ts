// LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

function minSessions(tasks: number[], sessionTime: number): number {
    const n = tasks.length;
    const INF = [n + 1, 0];
    const dp = Array.from({ length: 1 << n }, () => INF.slice());
    dp[0] = [1, 0];
    for (let mask = 0; mask < (1 << n); mask++) {
        const [sessions, used] = dp[mask];
        if (sessions > n) continue;
        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;
            const t = tasks[i];
            const nmask = mask | (1 << i);
            const cand = used + t <= sessionTime ? [sessions, used + t] : [sessions + 1, t];
            if (cand[0] < dp[nmask][0] || (cand[0] === dp[nmask][0] && cand[1] < dp[nmask][1])) {
                dp[nmask] = cand;
            }
        }
    }
    return dp[(1 << n) - 1][0];
}
