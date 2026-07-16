// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

class TrieNode {
    children = new Map<string, TrieNode>();
    word: string | null = null;
}

export function findWords(board: string[][], words: string[]): string[] {
    const root = new TrieNode();
    for (const word of words) {
        let node = root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.word = word;
    }

    const rows = board.length;
    const cols = board[0].length;
    const result = new Set<string>();
    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] as const;

    const dfs = (row: number, col: number, node: TrieNode): void => {
        const char = board[row][col];
        const next = node.children.get(char);
        if (!next) {
            return;
        }
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
}
