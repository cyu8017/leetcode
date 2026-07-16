// LeetCode 0208 - Implement Trie (Prefix Tree)\n// https://leetcode.com/problems/\n\nusing System.Collections.Generic;

public class Trie {
    private class TrieNode { public readonly Dictionary<char, TrieNode> Children = new(); public bool IsWord; }
    private readonly TrieNode root = new();

    public void Insert(string word) {
        var node = root;
        foreach (var c in word) { if (!node.Children.TryGetValue(c, out var child)) { child = new TrieNode(); node.Children[c] = child; } node = child; }
        node.IsWord = true;
    }

    public bool Search(string word) { var node = Find(word); return node != null && node.IsWord; }
    public bool StartsWith(string prefix) => Find(prefix) != null;

    private TrieNode Find(string text) {
        var node = root;
        foreach (var c in text) { if (!node.Children.TryGetValue(c, out node)) return null; }
        return node;
    }
}
