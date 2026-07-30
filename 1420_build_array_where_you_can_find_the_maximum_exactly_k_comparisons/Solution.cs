// LeetCode 1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
// https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

public class Solution {
    public int NumOfArrays(int n, int m, int k) {
        int mod = 1000000007;
        var dp = new int[k + 1, m + 1];
        for (int maximum = 1; maximum <= m; maximum++) dp[1, maximum] = 1;
        for (int len = 1; len < n; len++) {
            var nxt = new int[k + 1, m + 1];
            for (int cost = 1; cost <= k; cost++) {
                int prefix = 0;
                for (int maximum = 1; maximum <= m; maximum++) {
                    prefix = (prefix + dp[cost - 1, maximum - 1]) % mod;
                    nxt[cost, maximum] = (int)(((long)maximum * dp[cost, maximum] + prefix) % mod);
                }
            }
            dp = nxt;
        }
        int ans = 0;
        for (int maximum = 1; maximum <= m; maximum++) ans = (ans + dp[k, maximum]) % mod;
        return ans;
    }
}
