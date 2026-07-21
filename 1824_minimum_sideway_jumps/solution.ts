// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

function minSideJumps(obstacles: number[]): number {
    const INF = Number.POSITIVE_INFINITY;
    let dp = [1, 0, 1];
    for (const obs of obstacles) {
        const blocked = [obs === 1, obs === 2, obs === 3];
        const ndp = [INF, INF, INF];
        for (let lane = 0; lane < 3; lane++) {
            if (blocked[lane]) continue;
            for (let other = 0; other < 3; other++) {
                if (blocked[other] || dp[other] === INF) continue;
                ndp[lane] = Math.min(ndp[lane], dp[other] + (lane !== other ? 1 : 0));
            }
        }
        dp = ndp;
    }
    return Math.min(...dp);
}
