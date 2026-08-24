// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

class Solution {
    func findChampion(_ grid: [[Int]]) -> Int {
        let n = grid.count
        for i in 0..<n {
            var win = true
            for j in 0..<n where i != j && grid[i][j] == 0 {
                win = false
                break
            }
            if win { return i }
        }
        return -1
    }
}
