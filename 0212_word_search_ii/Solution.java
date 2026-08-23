// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    private static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        String word;
    }

    private char[][] board;
    private int rows;
    private int cols;
    private Set<String> result = new HashSet<>();

    public List<String> findWords(char[][] board, String[] words) {
        this.board = board;
        this.rows = board.length;
        this.cols = board[0].length;

        TrieNode root = new TrieNode();
        for (String word : words) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                node = node.children.computeIfAbsent(c, key -> new TrieNode());
            }
            node.word = word;
        }

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                dfs(row, col, root);
            }
        }
        return new ArrayList<>(result);
    }

    private void dfs(int row, int col, TrieNode node) {
        char c = board[row][col];
        TrieNode next = node.children.get(c);
        if (next == null) {
            return;
        }
        if (next.word != null) {
            result.add(next.word);
            next.word = null;
        }
        board[row][col] = '#';
        if (row + 1 < rows && board[row + 1][col] != '#') dfs(row + 1, col, next);
        if (row - 1 >= 0 && board[row - 1][col] != '#') dfs(row - 1, col, next);
        if (col + 1 < cols && board[row][col + 1] != '#') dfs(row, col + 1, next);
        if (col - 1 >= 0 && board[row][col - 1] != '#') dfs(row, col - 1, next);
        board[row][col] = c;
        if (next.children.isEmpty()) {
            node.children.remove(c);
        }
    }
}
