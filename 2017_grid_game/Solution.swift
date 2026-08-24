// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

class Solution {
    func gridGame(_ grid: [[Int]]) -> Int {
        let n = grid[0].count
        var top = grid[0].reduce(0, +)
        var bottom = 0
        var ans = Int.max
        for i in 0..<n {
            top -= grid[0][i]
            ans = min(ans, max(top, bottom))
            bottom += grid[1][i]
        }
        return ans
    }
}
