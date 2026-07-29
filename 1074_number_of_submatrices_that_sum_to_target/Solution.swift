// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution {
    func numSubmatrixSumTarget(_ matrix: [[Int]], _ target: Int) -> Int {
        let rows = matrix.count
        let cols = matrix[0].count
        var ans = 0
        for left in 0..<cols {
            var rowSum = Array(repeating: 0, count: rows)
            for right in left..<cols {
                for r in 0..<rows {
                    rowSum[r] += matrix[r][right]
                }
                var prefix = 0
                var seen: [Int: Int] = [0: 1]
                for val in rowSum {
                    prefix += val
                    ans += seen[prefix - target, default: 0]
                    seen[prefix, default: 0] += 1
                }
            }
        }
        return ans
    }
}
