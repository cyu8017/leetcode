// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

class Solution {
    func numDistinctIslands2(_ grid: [[Int]]) -> Int {
        var grid = grid
        guard !grid.isEmpty else { return 0 }
        let m = grid.count, n = grid[0].count
        var shapes = Set<String>()
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 {
                var cells = [[Int]]()
                dfs(&grid, i, j, m, n, &cells)
                shapes.insert(canonical(cells))
            }
        }
        return shapes.count
    }

    private func dfs(_ grid: inout [[Int]], _ r: Int, _ c: Int, _ m: Int, _ n: Int, _ cells: inout [[Int]]) {
        if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 { return }
        grid[r][c] = 0
        cells.append([r, c])
        dfs(&grid, r + 1, c, m, n, &cells)
        dfs(&grid, r - 1, c, m, n, &cells)
        dfs(&grid, r, c + 1, m, n, &cells)
        dfs(&grid, r, c - 1, m, n, &cells)
    }

    private func canonical(_ cells: [[Int]]) -> String {
        let signs = [[1, 1, 0], [1, -1, 0], [-1, 1, 0], [-1, -1, 0],
                     [1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1]]
        var best: String? = nil
        for s in signs {
            var pts = [[Int]]()
            for p in cells {
                let x = p[0], y = p[1]
                if s[2] == 0 { pts.append([s[0] * x, s[1] * y]) }
                else { pts.append([s[0] * y, s[1] * x]) }
            }
            let minX = pts.map { $0[0] }.min()!
            let minY = pts.map { $0[1] }.min()!
            for i in 0..<pts.count {
                pts[i][0] -= minX
                pts[i][1] -= minY
            }
            pts.sort { $0[0] != $1[0] ? $0[0] < $1[0] : $0[1] < $1[1] }
            let key = pts.map { "\($0[0]),\($0[1])" }.joined(separator: ";")
            if best == nil || key < best! { best = key }
        }
        return best!
    }
}
