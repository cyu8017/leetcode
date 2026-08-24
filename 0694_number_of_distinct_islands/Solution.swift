// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

class Solution {
    func numDistinctIslands(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        var shapes = Set<String>()
        func dfs(_ r: Int, _ c: Int, _ br: Int, _ bc: Int, _ path: inout [String]) {
            if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 { return }
            grid[r][c] = 0
            path.append("\(r - br),\(c - bc)")
            dfs(r + 1, c, br, bc, &path)
            dfs(r - 1, c, br, bc, &path)
            dfs(r, c + 1, br, bc, &path)
            dfs(r, c - 1, br, bc, &path)
        }
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 {
                var path = [String]()
                dfs(i, j, i, j, &path)
                shapes.insert(path.joined(separator: ";"))
            }
        }
        return shapes.count
    }
}
