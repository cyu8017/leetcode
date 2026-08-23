// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

import java.util.HashMap;
import java.util.Map;

class WordDictionary {
    private static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        boolean isWord;
    }

    private final TrieNode root = new TrieNode();

    public void addWord(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node = node.children.computeIfAbsent(c, key -> new TrieNode());
        }
        node.isWord = true;
    }

    public boolean search(String word) {
        return dfs(root, word, 0);
    }

    private boolean dfs(TrieNode node, String word, int index) {
        if (index == word.length()) {
            return node.isWord;
        }
        char c = word.charAt(index);
        if (c == '.') {
            for (TrieNode child : node.children.values()) {
                if (dfs(child, word, index + 1)) {
                    return true;
                }
            }
            return false;
        }
        TrieNode next = node.children.get(c);
        if (next == null) {
            return false;
        }
        return dfs(next, word, index + 1);
    }
}
