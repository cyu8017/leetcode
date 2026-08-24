// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

class Solution {
    func matrixMedian(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        let need = (m * n) / 2 + 1
        func countLE(_ x: Int) -> Int {
            var cnt = 0
            for row in grid {
                var l = 0, r = n
                while l < r {
                    let mid = (l + r) / 2
                    if row[mid] <= x { l = mid + 1 } else { r = mid }
                }
                cnt += l
            }
            return cnt
        }
        var lo = 1, hi = 1_000_000
        while lo < hi {
            let mid = (lo + hi) / 2
            if countLE(mid) >= need { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }
}
