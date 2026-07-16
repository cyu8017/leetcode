// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

class TrieNode {
    constructor() {
        this.children = new Map();
        this.word = null;
    }
}

/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(board, words) {
    const root = new TrieNode();
    for (const word of words) {
        let node = root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char);
        }
        node.word = word;
    }

    const rows = board.length;
    const cols = board[0].length;
    const result = new Set();
    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

    const dfs = (row, col, node) => {
        const char = board[row][col];
        if (!node.children.has(char)) {
            return;
        }
        const next = node.children.get(char);
        if (next.word) {
            result.add(next.word);
            next.word = null;
        }
        board[row][col] = '#';
        for (const [dr, dc] of directions) {
            const nr = row + dr;
            const nc = col + dc;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] !== '#') {
                dfs(nr, nc, next);
            }
        }
        board[row][col] = char;
        if (next.children.size === 0) {
            node.children.delete(char);
        }
    };

    for (let row = 0; row < rows; row += 1) {
        for (let col = 0; col < cols; col += 1) {
            dfs(row, col, root);
        }
    }
    return [...result];
};
