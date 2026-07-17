// LeetCode 1706 - Where Will the Ball Fall
// https://leetcode.com/problems/where-will-the-ball-fall/

class Solution {
    func findBall(_ grid: [[Int]]) -> [Int] {
        let m = grid.count
        let n = grid[0].count
        var ans = [Int]()
        for start in 0..<n {
            var col = start
            for row in 0..<m {
                let next = col + grid[row][col]
                if next < 0 || next == n || grid[row][next] != grid[row][col] {
                    col = -1
                    break
                }
                col = next
            }
            ans.append(col)
        }
        return ans
    }
}
