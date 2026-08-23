// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

using System.Collections.Generic;

public class Solution {
    private class TrieNode {
        public readonly Dictionary<char, TrieNode> Children = new();
        public string Word;
    }

    private char[][] board;
    private int rows;
    private int cols;
    private readonly HashSet<string> result = new();

    public IList<string> FindWords(char[][] board, string[] words) {
        this.board = board;
        rows = board.Length;
        cols = board[0].Length;

        var root = new TrieNode();
        foreach (var word in words) {
            var node = root;
            foreach (var c in word) {
                if (!node.Children.TryGetValue(c, out var child)) {
                    child = new TrieNode();
                    node.Children[c] = child;
                }
                node = child;
            }
            node.Word = word;
        }

        for (var row = 0; row < rows; row++) {
            for (var col = 0; col < cols; col++) {
                Dfs(row, col, root);
            }
        }
        return new List<string>(result);
    }

    private void Dfs(int row, int col, TrieNode node) {
        var c = board[row][col];
        if (!node.Children.TryGetValue(c, out var next)) return;
        if (next.Word != null) {
            result.Add(next.Word);
            next.Word = null;
        }
        board[row][col] = '#';
        if (row + 1 < rows && board[row + 1][col] != '#') Dfs(row + 1, col, next);
        if (row - 1 >= 0 && board[row - 1][col] != '#') Dfs(row - 1, col, next);
        if (col + 1 < cols && board[row][col + 1] != '#') Dfs(row, col + 1, next);
        if (col - 1 >= 0 && board[row][col - 1] != '#') Dfs(row, col - 1, next);
        board[row][col] = c;
        if (next.Children.Count == 0) node.Children.Remove(c);
    }
}
