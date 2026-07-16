// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

class TrieNode {
    var children = [Character: TrieNode]()
    var word: String?
}

class Solution {
    private var board: [[Character]] = []
    private var rows = 0
    private var cols = 0
    private var result = Set<String>()

    func findWords(_ board: [[Character]], _ words: [String]) -> [String] {
        self.board = board
        rows = board.count
        cols = board[0].count

        let root = TrieNode()
        for word in words {
            var node = root
            for char in word {
                if node.children[char] == nil {
                    node.children[char] = TrieNode()
                }
                node = node.children[char]!
            }
            node.word = word
        }

        for row in 0..<rows {
            for col in 0..<cols {
                dfs(row, col, root)
            }
        }
        return Array(result)
    }

    private func dfs(_ row: Int, _ col: Int, _ node: TrieNode) {
        let char = board[row][col]
        guard let next = node.children[char] else { return }
        if let word = next.word {
            result.insert(word)
            next.word = nil
        }
        board[row][col] = "#"
        if row + 1 < rows && board[row + 1][col] != "#" { dfs(row + 1, col, next) }
        if row - 1 >= 0 && board[row - 1][col] != "#" { dfs(row - 1, col, next) }
        if col + 1 < cols && board[row][col + 1] != "#" { dfs(row, col + 1, next) }
        if col - 1 >= 0 && board[row][col - 1] != "#" { dfs(row, col - 1, next) }
        board[row][col] = char
        if next.children.isEmpty {
            node.children.removeValue(forKey: char)
        }
    }
}
