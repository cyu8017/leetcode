// LeetCode 1351 - Count Negative Numbers in a Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution {
    func countNegatives(_ grid: [[Int]]) -> Int {
        var ans = 0
        for row in grid {
            var lo = 0, hi = row.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if row[mid] < 0 { hi = mid } else { lo = mid + 1 }
            }
            ans += row.count - lo
        }
        return ans
    }
}
