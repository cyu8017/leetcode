// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

class Solution {
    func minScore(_ grid: [[Int]]) -> [[Int]] {
        let m = grid.count, n = grid[0].count
        var arr: [(Int, Int, Int)] = []
        for i in 0..<m {
            for j in 0..<n { arr.append((grid[i][j], i, j)) }
        }
        arr.sort { $0.0 < $1.0 }
        var rowMax = [Int](repeating: 0, count: m)
        var colMax = [Int](repeating: 0, count: n)
        var ans = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        for cel in arr {
            let val = max(rowMax[cel.1], colMax[cel.2]) + 1
            ans[cel.1][cel.2] = val
            rowMax[cel.1] = val
            colMax[cel.2] = val
        }
        return ans
    }
}
