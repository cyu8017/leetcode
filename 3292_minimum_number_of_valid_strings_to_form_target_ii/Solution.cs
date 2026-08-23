// LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

public class Solution {
    class TrieNode {
        public TrieNode[] next = new TrieNode[26];
    }

    public int MinValidStrings(string[] words, string target) {
        int n = target.Length;
        const int inf = 1000000000;
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = inf;
        dp[0] = 0;
        var root = new TrieNode();
        foreach (string w in words) {
            var cur = root;
            foreach (char c in w) {
                int ci = c - 'a';
                if (cur.next[ci] == null) cur.next[ci] = new TrieNode();
                cur = cur.next[ci];
            }
        }
        for (int i = 0; i < n; i++) {
            if (dp[i] == inf) continue;
            var cur = root;
            for (int j = i; j < n; j++) {
                int ci = target[j] - 'a';
                if (cur.next[ci] == null) break;
                cur = cur.next[ci];
                if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
            }
        }
        return dp[n] == inf ? -1 : dp[n];
    }
}
