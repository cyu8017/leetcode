// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

using System.Collections.Generic;

public class StreamChecker {
    private class TrieNode {
        public readonly Dictionary<char, TrieNode> Children = new();
        public bool IsWord;
    }

    private readonly TrieNode root = new();
    private readonly List<char> stream = new();

    public StreamChecker(string[] words) {
        foreach (string word in words) {
            var node = root;
            for (int i = word.Length - 1; i >= 0; i--) {
                char ch = word[i];
                if (!node.Children.TryGetValue(ch, out var child)) {
                    child = new TrieNode();
                    node.Children[ch] = child;
                }
                node = child;
            }
            node.IsWord = true;
        }
    }

    public bool Query(char letter) {
        stream.Add(letter);
        var node = root;
        for (int i = stream.Count - 1; i >= 0; i--) {
            if (node.IsWord) return true;
            if (!node.Children.TryGetValue(stream[i], out node)) return false;
        }
        return node.IsWord;
    }
}
