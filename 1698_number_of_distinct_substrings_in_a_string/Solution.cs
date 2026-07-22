// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

using System.Collections.Generic;

public class Solution {
    public int CountDistinct(string s) {
        var trie = new TrieNode();
        int ans = 0;
        for (int i = 0; i < s.Length; i++) {
            TrieNode node = trie;
            for (int j = i; j < s.Length; j++) {
                char c = s[j];
                if (!node.Next.TryGetValue(c, out var child)) {
                    child = new TrieNode();
                    node.Next[c] = child;
                    ans++;
                }
                node = child;
            }
        }
        return ans;
    }

    private class TrieNode {
        public readonly Dictionary<char, TrieNode> Next = new();
    }
}
