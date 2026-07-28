// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

public class Solution {
    public int MergeStones(int[] stones, int k) {
        int n = stones.Length;
        if ((n - 1) % (k - 1) != 0) return -1;
        var prefix = new int[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + stones[i];
        var dp = new int[n, n];
        for (int length = k; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                int best = int.MaxValue;
                for (int m = i; m < j; m += k - 1)
                    best = Math.Min(best, dp[i, m] + dp[m + 1, j]);
                dp[i, j] = best;
                if ((length - 1) % (k - 1) == 0)
                    dp[i, j] += prefix[j + 1] - prefix[i];
            }
        }
        return dp[0, n - 1];
    }
}
