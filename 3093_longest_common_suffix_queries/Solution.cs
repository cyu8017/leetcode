// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

public class Solution {
    const int INF = 1 << 30;
    class Trie {
        public Trie[] Children = new Trie[26];
        public int Length = INF;
        public int Idx = INF;
    }

    static void Insert(Trie t, string w, int i) {
        Trie node = t;
        if (node.Length > w.Length) {
            node.Length = w.Length;
            node.Idx = i;
        }
        for (int k = w.Length - 1; k >= 0; k--) {
            int id = w[k] - 'a';
            if (node.Children[id] == null) node.Children[id] = new Trie();
            node = node.Children[id];
            if (node.Length > w.Length) {
                node.Length = w.Length;
                node.Idx = i;
            }
        }
    }

    static int Query(Trie t, string w) {
        Trie node = t;
        for (int k = w.Length - 1; k >= 0; k--) {
            int id = w[k] - 'a';
            if (node.Children[id] == null) break;
            node = node.Children[id];
        }
        return node.Idx;
    }

    public int[] StringIndices(string[] wordsContainer, string[] wordsQuery) {
        Trie trie = new Trie();
        for (int i = 0; i < wordsContainer.Length; i++) Insert(trie, wordsContainer[i], i);
        int[] ans = new int[wordsQuery.Length];
        for (int i = 0; i < wordsQuery.Length; i++) ans[i] = Query(trie, wordsQuery[i]);
        return ans;
    }
}
