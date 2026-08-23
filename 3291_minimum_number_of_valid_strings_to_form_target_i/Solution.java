// LeetCode 3291 - Minimum Number of Valid Strings to Form Target I
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

import java.util.Arrays;

class Solution {
    static class TrieNode {
        TrieNode[] next = new TrieNode[26];
    }

    public int minValidStrings(String[] words, String target) {
        int n = target.length();
        final int inf = 1_000_000_000;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, inf);
        dp[0] = 0;
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode cur = root;
            for (char c : w.toCharArray()) {
                int ci = c - 'a';
                if (cur.next[ci] == null) cur.next[ci] = new TrieNode();
                cur = cur.next[ci];
            }
        }
        for (int i = 0; i < n; i++) {
            if (dp[i] == inf) continue;
            TrieNode cur = root;
            for (int j = i; j < n; j++) {
                int ci = target.charAt(j) - 'a';
                if (cur.next[ci] == null) break;
                cur = cur.next[ci];
                if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
            }
        }
        return dp[n] == inf ? -1 : dp[n];
    }
}
