// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class Solution {
    private class TrieNode {
        public TrieNode[] Child = new TrieNode[26];
        public int Cnt;
    }

    public int[] sumPrefixScores(String[] words) {
        var root = new TrieNode();
        for (String w : words) {
            TrieNode cur = root;
            for (char ch : w) {
                int c = ch - 'a';
                if (cur.Child[c] == null) cur.Child[c] = new TrieNode();
                cur = cur.Child[c];
                cur.Cnt++;
            }
        }
        int[] ans = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            TrieNode cur = root;
            int sum = 0;
            for (char ch : words[i]) {
                cur = cur.Child[ch - 'a'];
                sum += cur.Cnt;
            }
            ans[i] = sum;
        }
        return ans;
    }
}
