// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

public class Solution {
    public int CountWays(string word1, string word2, string target) {
        const int mod = 1000000007;
        int n1 = word1.Length;
        int n2 = word2.Length;
        int size = (n1 + 1) * (n2 + 1) * 4;
        int Index(int i, int j, int mask) {
            return ((i * (n2 + 1) + j) * 4) + mask;
        }
        int[] dp = new int[size], next = new int[size];
        dp[Index(0, 0, 0)] = 1;
        foreach (char ch in target) {
            System.Array.Fill(next, 0);
            for (int j = 0; j <= n2; j++) {
                int[] prefix = new int[4];
                for (int a = 0; a < n1; a++) {
                    for (int mask = 0; mask < 4; mask++) {
                        prefix[mask] += dp[Index(a, j, mask)];
                        if (prefix[mask] >= mod) prefix[mask] -= mod;
                    }
                    if (word1[a] == ch) {
                        for (int mask = 0; mask < 4; mask++) {
                            int at = Index(a + 1, j, mask | 1);
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
                        prefix[mask] += dp[Index(i, b, mask)];
                        if (prefix[mask] >= mod) prefix[mask] -= mod;
                    }
                    if (word2[b] == ch) {
                        for (int mask = 0; mask < 4; mask++) {
                            int at = Index(i, b + 1, mask | 2);
                            next[at] += prefix[mask];
                            if (next[at] >= mod) next[at] -= mod;
                        }
                    }
                }
            }
            var tmp = dp; dp = next; next = tmp;
        }
        int answer = 0;
        for (int i = 0; i <= n1; i++) {
            for (int j = 0; j <= n2; j++) {
                answer += dp[Index(i, j, 3)];
                if (answer >= mod) answer -= mod;
            }
        }
        return answer;
    }
}
