// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

#define INF 1000000000

int minSideJumps(int* obstacles, int obstaclesSize) {
    int dp[3] = {1, 0, 1};
    for (int i = 0; i < obstaclesSize; i++) {
        int obs = obstacles[i];
        int blocked[3];
        for (int lane = 0; lane < 3; lane++) blocked[lane] = (obs == lane + 1);
        int ndp[3] = {INF, INF, INF};
        for (int lane = 0; lane < 3; lane++) {
            if (blocked[lane]) continue;
            for (int other = 0; other < 3; other++) {
                if (blocked[other] || dp[other] == INF) continue;
                int cand = dp[other] + (lane != other);
                if (cand < ndp[lane]) ndp[lane] = cand;
            }
        }
        dp[0] = ndp[0];
        dp[1] = ndp[1];
        dp[2] = ndp[2];
    }
    int best = dp[0];
    if (dp[1] < best) best = dp[1];
    if (dp[2] < best) best = dp[2];
    return best;
}
