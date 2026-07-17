// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

import java.util.HashMap;
import java.util.Map;

class Trie {
    private static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        int wordCount;
        int prefixCount;
    }

    private final TrieNode root = new TrieNode();

    public Trie() {
    }

    public void insert(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            node = node.children.computeIfAbsent(ch, key -> new TrieNode());
            node.prefixCount++;
        }
        node.wordCount++;
    }

    public int countWordsEqualTo(String word) {
        TrieNode node = find(word);
        return node != null ? node.wordCount : 0;
    }

    public int countWordsStartingWith(String prefix) {
        TrieNode node = find(prefix);
        return node != null ? node.prefixCount : 0;
    }

    public void erase(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            node = node.children.get(ch);
            node.prefixCount--;
        }
        node.wordCount--;
    }

    private TrieNode find(String text) {
        TrieNode node = root;
        for (char ch : text.toCharArray()) {
            node = node.children.get(ch);
            if (node == null) {
                return null;
            }
        }
        return node;
    }
}
