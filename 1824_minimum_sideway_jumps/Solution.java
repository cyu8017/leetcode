// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

class Solution {
    public int minSideJumps(int[] obstacles) {
        int inf = Integer.MAX_VALUE / 4;
        int[] dp = {1, 0, 1};

        for (int obs : obstacles) {
            boolean[] blocked = {obs == 1, obs == 2, obs == 3};
            int[] ndp = {inf, inf, inf};
            for (int lane = 0; lane < 3; lane++) {
                if (blocked[lane]) {
                    continue;
                }
                for (int other = 0; other < 3; other++) {
                    if (blocked[other] || dp[other] == inf) {
                        continue;
                    }
                    ndp[lane] = Math.min(ndp[lane], dp[other] + (lane != other ? 1 : 0));
                }
            }
            dp = ndp;
        }

        return Math.min(dp[0], Math.min(dp[1], dp[2]));
    }
}
