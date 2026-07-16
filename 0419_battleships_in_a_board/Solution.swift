// LeetCode 0419 - Battleships in a Board
// https://leetcode.com/problems/battleships-in-a-board/

class Solution {
    func countBattleships(_ board: [[Character]]) -> Int {
        var count = 0
        for row in 0..<board.count {
            for col in 0..<board[0].count {
                if board[row][col] != "X" {
                    continue
                }
                if row > 0 && board[row - 1][col] == "X" {
                    continue
                }
                if col > 0 && board[row][col - 1] == "X" {
                    continue
                }
                count += 1
            }
        }
        return count
    }
}
