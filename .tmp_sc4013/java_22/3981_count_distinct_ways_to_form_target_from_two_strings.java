// CONFIG class=Solution method=countWays types=None
// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

import java.util.Arrays;

class Solution {
    public int countWays(String word1, String word2, String target) {
        final int mod = 1000000007;
        int n1 = word1.length(), n2 = word2.length();
        int size = (n1 + 1) * (n2 + 1) * 4;
        int[] dp = new int[size], next = new int[size];
        dp[index(0, 0, 0, n2)] = 1;
        for (int ti = 0; ti < target.length(); ti++) {
            char ch = target.charAt(ti);
            Arrays.fill(next, 0);
            for (int j = 0; j <= n2; j++) {
                int[] prefix = new int[4];
                for (int a = 0; a < n1; a++) {
                    for (int mask = 0; mask < 4; mask++) {
                        prefix[mask] += dp[index(a, j, mask, n2)];
                        if (prefix[mask] >= mod) prefix[mask] -= mod;
                    }
                    if (word1.charAt(a) == ch) {
                        for (int mask = 0; mask < 4; mask++) {
                            int at = index(a + 1, j, mask | 1, n2);
                            next[at] += prefix[mask];
                            if (next[at] >= mod) next[at] -= mod;
                        }
                    }
                }
            }
            for (int i = 0; i <= n1; i++) {
                int[] prefix = new int[4];
                for (int b = 0; b < n2; b++) {
                    for (int mask = 0; mask < 4; mask++) {
                        prefix[mask] += dp[index(i, b, mask, n2)];
                        if (prefix[mask] >= mod) prefix[mask] -= mod;
                    }
                    if (word2.charAt(b) == ch) {
                        for (int mask = 0; mask < 4; mask++) {
                            int at = index(i, b + 1, mask | 2, n2);
                            next[at] += prefix[mask];
                            if (next[at] >= mod) next[at] -= mod;
                        }
                    }
                }
            }
            int[] tmp = dp; dp = next; next = tmp;
        }
        int answer = 0;
        for (int i = 0; i <= n1; i++) {
            for (int j = 0; j <= n2; j++) {
                answer += dp[index(i, j, 3, n2)];
                if (answer >= mod) answer -= mod;
            }
        }
        return answer;
    }

    private int index(int i, int j, int mask, int n2) {
        return ((i * (n2 + 1) + j) * 4) + mask;
    }
}
