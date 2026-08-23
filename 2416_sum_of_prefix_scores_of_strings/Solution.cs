// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

public class Solution {
    private class TrieNode {
        public TrieNode[] Child = new TrieNode[26];
        public int Cnt;
    }

    public int[] SumPrefixScores(string[] words) {
        var root = new TrieNode();
        foreach (string w in words) {
            TrieNode cur = root;
            foreach (char ch in w) {
                int c = ch - 'a';
                if (cur.Child[c] == null) cur.Child[c] = new TrieNode();
                cur = cur.Child[c];
                cur.Cnt++;
            }
        }
        int[] ans = new int[words.Length];
        for (int i = 0; i < words.Length; i++) {
            TrieNode cur = root;
            int sum = 0;
            foreach (char ch in words[i]) {
                cur = cur.Child[ch - 'a'];
                sum += cur.Cnt;
            }
            ans[i] = sum;
        }
        return ans;
    }
}
