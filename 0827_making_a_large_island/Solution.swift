// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

class Solution {
    func largestIsland(_ grid: [[Int]]) -> Int {
        var grid = grid
        let n = grid.count
        var sizes = [0: 0]
        var islandId = 2
        func dfs(_ r: Int, _ c: Int, _ iid: Int) -> Int {
            if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1 { return 0 }
            grid[r][c] = iid
            return 1 + dfs(r + 1, c, iid) + dfs(r - 1, c, iid) + dfs(r, c + 1, iid) + dfs(r, c - 1, iid)
        }
        for i in 0..<n {
            for j in 0..<n {
                if grid[i][j] == 1 {
                    sizes[islandId] = dfs(i, j, islandId)
                    islandId += 1
                }
            }
        }
        var ans = sizes.values.max() ?? 0
        let dr = [1, -1, 0, 0], dc = [0, 0, 1, -1]
        for i in 0..<n {
            for j in 0..<n {
                if grid[i][j] != 0 { continue }
                var seen = Set<Int>()
                var total = 1
                for k in 0..<4 {
                    let ni = i + dr[k], nj = j + dc[k]
                    if ni >= 0 && ni < n && nj >= 0 && nj < n {
                        let iid = grid[ni][nj]
                        if iid > 1 && seen.insert(iid).inserted {
                            total += sizes[iid] ?? 0
                        }
                    }
                }
                ans = max(ans, total)
            }
        }
        return ans
    }
}
