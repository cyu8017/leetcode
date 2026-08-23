// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

class Solution {
    private static final int INF = 1 << 30;

    static class Trie {
        Trie[] children = new Trie[26];
        int length = INF;
        int idx = INF;
    }

    private void insert(Trie t, String w, int i) {
        Trie node = t;
        if (node.length > w.length()) {
            node.length = w.length();
            node.idx = i;
        }
        for (int k = w.length() - 1; k >= 0; k--) {
            int id = w.charAt(k) - 'a';
            if (node.children[id] == null) node.children[id] = new Trie();
            node = node.children[id];
            if (node.length > w.length()) {
                node.length = w.length();
                node.idx = i;
            }
        }
    }

    private int query(Trie t, String w) {
        Trie node = t;
        for (int k = w.length() - 1; k >= 0; k--) {
            int id = w.charAt(k) - 'a';
            if (node.children[id] == null) break;
            node = node.children[id];
        }
        return node.idx;
    }

    public int[] stringIndices(String[] wordsContainer, String[] wordsQuery) {
        Trie trie = new Trie();
        for (int i = 0; i < wordsContainer.length; i++) insert(trie, wordsContainer[i], i);
        int[] ans = new int[wordsQuery.length];
        for (int i = 0; i < wordsQuery.length; i++) ans[i] = query(trie, wordsQuery[i]);
        return ans;
    }
}
