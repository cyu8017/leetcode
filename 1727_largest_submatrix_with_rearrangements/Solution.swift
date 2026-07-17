// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

class Solution {
    func largestSubmatrix(_ matrix: [[Int]]) -> Int {
        let m = matrix.count
        let n = matrix[0].count
        var heights = [Int](repeating: 0, count: n)
        var best = 0
        for r in 0..<m {
            for c in 0..<n {
                heights[c] = matrix[r][c] == 1 ? heights[c] + 1 : 0
            }
            let sorted = heights.sorted(by: >)
            for width in 1...n {
                best = max(best, width * sorted[width - 1])
            }
        }
        return best
    }
}
