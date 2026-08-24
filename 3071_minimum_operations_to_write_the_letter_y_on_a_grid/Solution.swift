// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

class Solution {
    func minimumOperationsToWriteY(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var cnt1 = [0, 0, 0], cnt2 = [0, 0, 0]
        for i in 0..<n {
            for j in 0..<n {
                let x = grid[i][j]
                let a = i == j && i <= n / 2
                let b = i + j == n - 1 && i <= n / 2
                let c = j == n / 2 && i >= n / 2
                if a || b || c { cnt1[x] += 1 }
                else { cnt2[x] += 1 }
            }
        }
        var ans = n * n
        for i in 0..<3 {
            for j in 0..<3 where i != j {
                ans = min(ans, n * n - cnt1[i] - cnt2[j])
            }
        }
        return ans
    }
}
