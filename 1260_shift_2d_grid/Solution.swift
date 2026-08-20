// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

class Solution {
    func shiftGrid(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        let m = grid.count, n = grid[0].count
        let total = m * n
        let k = k % total
        var flat = grid.flatMap { $0 }
        flat = Array(flat[(total - k)...]) + Array(flat[..<(total - k)])
        var ans = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        for i in 0..<total { ans[i / n][i % n] = flat[i] }
        return ans
    }
}
