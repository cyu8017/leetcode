// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

using System.Collections.Generic;

public class WordDictionary {
    private class TrieNode {
        public readonly Dictionary<char, TrieNode> Children = new();
        public bool IsWord;
    }

    private readonly TrieNode root = new();

    public void AddWord(string word) {
        var node = root;
        foreach (var c in word) {
            if (!node.Children.TryGetValue(c, out var child)) {
                child = new TrieNode();
                node.Children[c] = child;
            }
            node = child;
        }
        node.IsWord = true;
    }

    public bool Search(string word) => Dfs(root, word, 0);

    private bool Dfs(TrieNode node, string word, int index) {
        if (index == word.Length) return node.IsWord;
        var c = word[index];
        if (c == '.') {
            foreach (var child in node.Children.Values) {
                if (Dfs(child, word, index + 1)) return true;
            }
            return false;
        }
        if (!node.Children.TryGetValue(c, out var next)) return false;
        return Dfs(next, word, index + 1);
    }
}
