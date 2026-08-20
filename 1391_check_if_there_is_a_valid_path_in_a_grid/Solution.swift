// LeetCode 1391 - Check if There is a Valid Path in a Grid
// https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution {
    func hasValidPath(_ grid: [[Int]]) -> Bool {
        let dirs: [Int: [(Int, Int)]] = [
            1: [(0, -1), (0, 1)], 2: [(-1, 0), (1, 0)], 3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)], 5: [(0, -1), (-1, 0)], 6: [(0, 1), (-1, 0)]
        ]
        let m = grid.count, n = grid[0].count
        var seen: Set<[Int]> = [[0, 0]]
        var st = [(0, 0)]
        while !st.isEmpty {
            let (r, c) = st.removeLast()
            if r == m - 1 && c == n - 1 { return true }
            for (dr, dc) in dirs[grid[r][c]]! {
                let x = r + dr, y = c + dc
                if x >= 0 && x < m && y >= 0 && y < n && !seen.contains([x, y])
                    && dirs[grid[x][y]]!.contains(where: { $0 == (-dr, -dc) }) {
                    seen.insert([x, y]); st.append((x, y))
                }
            }
        }
        return false
    }
}
