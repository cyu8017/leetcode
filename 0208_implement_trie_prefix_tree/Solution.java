// LeetCode 0208 - Implement Trie (Prefix Tree)\n// https://leetcode.com/problems/\n\nimport java.util.HashMap;
import java.util.Map;

class Trie {
    private static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        boolean isWord;
    }

    private final TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) node = node.children.computeIfAbsent(c, key -> new TrieNode());
        node.isWord = true;
    }

    public boolean search(String word) {
        TrieNode node = find(word);
        return node != null && node.isWord;
    }

    public boolean startsWith(String prefix) { return find(prefix) != null; }

    private TrieNode find(String text) {
        TrieNode node = root;
        for (char c : text.toCharArray()) {
            node = node.children.get(c);
            if (node == null) return null;
        }
        return node;
    }
}
