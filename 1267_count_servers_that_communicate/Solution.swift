// LeetCode 1267 - Count Servers that Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

class Solution {
    func countServers(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var rows = [Int](repeating: 0, count: m)
        var cols = [Int](repeating: 0, count: n)
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 {
                rows[i] += 1; cols[j] += 1
            }
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1) {
                ans += 1
            }
        }
        return ans
    }
}
