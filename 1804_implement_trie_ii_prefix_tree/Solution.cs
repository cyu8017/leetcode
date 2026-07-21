// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

using System.Collections.Generic;

public class Trie {
    private class TrieNode {
        public readonly Dictionary<char, TrieNode> Children = new();
        public int WordCount;
        public int PrefixCount;
    }

    private readonly TrieNode root = new();

    public void Insert(string word) {
        var node = root;
        foreach (char ch in word) {
            if (!node.Children.TryGetValue(ch, out var child)) {
                child = new TrieNode();
                node.Children[ch] = child;
            }
            node = child;
            node.PrefixCount++;
        }
        node.WordCount++;
    }

    public int CountWordsEqualTo(string word) {
        var node = Find(word);
        return node?.WordCount ?? 0;
    }

    public int CountWordsStartingWith(string prefix) {
        var node = Find(prefix);
        return node?.PrefixCount ?? 0;
    }

    public void Erase(string word) {
        var node = root;
        foreach (char ch in word) {
            node = node.Children[ch];
            node.PrefixCount--;
        }
        node.WordCount--;
    }

    private TrieNode Find(string text) {
        var node = root;
        foreach (char ch in text) {
            if (!node.Children.TryGetValue(ch, out node)) return null;
        }
        return node;
    }
}
