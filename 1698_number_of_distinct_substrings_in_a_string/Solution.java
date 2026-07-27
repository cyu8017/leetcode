// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

class Solution {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
    }

    public int countDistinct(String s) {
        TrieNode root = new TrieNode();
        int ans = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            TrieNode node = root;
            for (int j = i; j < n; j++) {
                int c = s.charAt(j) - 'a';
                if (node.children[c] == null) {
                    node.children[c] = new TrieNode();
                    ans++;
                }
                node = node.children[c];
            }
        }
        return ans;
    }
}
