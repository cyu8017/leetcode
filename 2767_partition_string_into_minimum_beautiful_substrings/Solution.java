// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minimumBeautifulSubstrings(String s) {
        int n = s.length();
        Set<String> pow5 = new HashSet<>();
        for (long x = 1; ; x *= 5) {
            String b = Long.toBinaryString(x);
            if (b.length() > n) break;
            pow5.add(b);
        }
        final int INF = 1 << 30;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == INF || s.charAt(i) == '0') continue;
            for (int j = i + 1; j <= n; j++) {
                if (pow5.contains(s.substring(i, j)))
                    dp[j] = Math.min(dp[j], dp[i] + 1);
            }
        }
        return dp[n] == INF ? -1 : dp[n];
    }
}
