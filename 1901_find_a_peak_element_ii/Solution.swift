// LeetCode 1901 - Find a Peak Element II
// https://leetcode.com/problems/find-a-peak-element-ii/

class Solution {
    func findPeakGrid(_ mat: [[Int]]) -> [Int] {
        let rows = mat.count
        let cols = mat[0].count
        var lo = 0
        var hi = cols - 1
        while lo <= hi {
            let mid = (lo + hi) / 2
            var maxRow = 0
            for r in 1..<rows {
                if mat[r][mid] > mat[maxRow][mid] { maxRow = r }
            }
            let left = mid > 0 ? mat[maxRow][mid - 1] : -1
            let right = mid + 1 < cols ? mat[maxRow][mid + 1] : -1
            if mat[maxRow][mid] >= left && mat[maxRow][mid] >= right {
                return [maxRow, mid]
            }
            if left > mat[maxRow][mid] {
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        return [0, 0]
    }
}
