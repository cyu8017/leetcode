// LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
// https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

class Solution {
    func countSortedMatrices(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count, n = grid[0].count
        var ans = 0
        for r1 in 0..<m {
            for r2 in r1..<m {
                for c1 in 0..<n {
                    for c2 in c1..<n {
                        var ok = true
                        var i = r1
                        while i <= r2 && ok {
                            for j in c1...c2 {
                                if grid[i][j] > k { ok = false; break }
                                if j > c1 && grid[i][j] < grid[i][j - 1] { ok = false; break }
                                if i > r1 && grid[i][j] < grid[i - 1][j] { ok = false; break }
                            }
                            i += 1
                        }
                        if ok { ans += 1 }
                    }
                }
            }
        }
        return ans
    }
}
