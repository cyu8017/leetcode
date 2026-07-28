// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

class StreamChecker {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isWord;
    }

    private final TrieNode root = new TrieNode();
    private final StringBuilder stream = new StringBuilder();

    public StreamChecker(String[] words) {
        for (String word : words) {
            TrieNode node = root;
            for (int i = word.length() - 1; i >= 0; i--) {
                int idx = word.charAt(i) - 'a';
                if (node.children[idx] == null) node.children[idx] = new TrieNode();
                node = node.children[idx];
            }
            node.isWord = true;
        }
    }

    public boolean query(String letter) {
        return query(letter.charAt(0));
    }

    public boolean query(char letter) {
        stream.append(letter);
        TrieNode node = root;
        for (int i = stream.length() - 1; i >= 0; i--) {
            if (node.isWord) return true;
            int idx = stream.charAt(i) - 'a';
            if (node.children[idx] == null) return false;
            node = node.children[idx];
        }
        return node.isWord;
    }
}
