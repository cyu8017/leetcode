// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

class Solution {
    func minimumMoves(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var q: [(Int, Int, Int, Int)] = [(0, 0, 0, 0)] // r,c,horiz?,dist
        var seen = Set<Int>([0])
        func key(_ r: Int, _ c: Int, _ h: Int) -> Int { (r * n + c) * 2 + h }
        var qi = 0
        while qi < q.count {
            let (r, c, h, d) = q[qi]; qi += 1
            if r == n - 1 && c == n - 2 && h == 0 { return d }
            if h == 0 {
                if c + 2 < n && grid[r][c + 2] == 0 {
                    let k = key(r, c + 1, 0)
                    if !seen.contains(k) { seen.insert(k); q.append((r, c + 1, 0, d + 1)) }
                }
                if r + 1 < n && grid[r + 1][c] == 0 && grid[r + 1][c + 1] == 0 {
                    let k1 = key(r + 1, c, 0)
                    if !seen.contains(k1) { seen.insert(k1); q.append((r + 1, c, 0, d + 1)) }
                    let k2 = key(r, c, 1)
                    if !seen.contains(k2) { seen.insert(k2); q.append((r, c, 1, d + 1)) }
                }
            } else {
                if r + 2 < n && grid[r + 2][c] == 0 {
                    let k = key(r + 1, c, 1)
                    if !seen.contains(k) { seen.insert(k); q.append((r + 1, c, 1, d + 1)) }
                }
                if c + 1 < n && grid[r][c + 1] == 0 && grid[r + 1][c + 1] == 0 {
                    let k1 = key(r, c + 1, 1)
                    if !seen.contains(k1) { seen.insert(k1); q.append((r, c + 1, 1, d + 1)) }
                    let k2 = key(r, c, 0)
                    if !seen.contains(k2) { seen.insert(k2); q.append((r, c, 0, d + 1)) }
                }
            }
        }
        return -1
    }
}
