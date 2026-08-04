// LeetCode 1335 - Minimum Difficulty Of A Job Schedule
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.length;
        if (n < d) return -1;
        var dp = new int[n];
        int hardest = 0;
        for (int i = 0; i < n; i++) { hardest = Math.max(hardest, jobDifficulty[i]); dp[i] = hardest; }
        for (int day = 1; day < d; day++) {
            var nxt = new int[n];
            for (int i = 0; i < n; i++) nxt[i] = 1000000000;
            for (int end = day; end < n; end++) {
                hardest = 0;
                for (int start = end; start >= day; start--) {
                    hardest = Math.max(hardest, jobDifficulty[start]);
                    nxt[end] = Math.min(nxt[end], dp[start - 1] + hardest);
                }
            }
            dp = nxt;
        }
        return dp[n - 1];
    }
}
