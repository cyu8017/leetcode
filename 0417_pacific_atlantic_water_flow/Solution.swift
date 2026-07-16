// LeetCode 0417 - Pacific Atlantic Water Flow
// https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution {
    func pacificAtlantic(_ heights: [[Int]]) -> [[Int]] {
        if heights.isEmpty || heights[0].isEmpty {
            return []
        }

        let rows = heights.count
        let cols = heights[0].count
        var pacific: Set<String> = []
        var atlantic: Set<String> = []

        for row in 0..<rows {
            dfs(heights, row, 0, &pacific, heights[row][0])
            dfs(heights, row, cols - 1, &atlantic, heights[row][cols - 1])
        }
        for col in 0..<cols {
            dfs(heights, 0, col, &pacific, heights[0][col])
            dfs(heights, rows - 1, col, &atlantic, heights[rows - 1][col])
        }

        return pacific.intersection(atlantic).map { key in
            let parts = key.split(separator: ",")
            return [Int(parts[0])!, Int(parts[1])!]
        }
    }

    private func dfs(
        _ heights: [[Int]],
        _ row: Int,
        _ col: Int,
        _ visited: inout Set<String>,
        _ previous: Int
    ) {
        let key = "\(row),\(col)"
        if visited.contains(key) {
            return
        }
        if row < 0 || row >= heights.count || col < 0 || col >= heights[0].count {
            return
        }
        if heights[row][col] < previous {
            return
        }

        visited.insert(key)
        let height = heights[row][col]
        dfs(heights, row + 1, col, &visited, height)
        dfs(heights, row - 1, col, &visited, height)
        dfs(heights, row, col + 1, &visited, height)
        dfs(heights, row, col - 1, &visited, height)
    }
}
