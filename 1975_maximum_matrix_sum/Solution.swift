// LeetCode 1975 - Maximum Matrix Sum
// https://leetcode.com/problems/maximum-matrix-sum/

class Solution {
    func maxMatrixSum(_ matrix: [[Int]]) -> Int {
        var total = 0, neg = 0, mn = Int.max
        for row in matrix {
            for x in row {
                if x < 0 { neg += 1 }
                let ax = abs(x)
                total += ax
                mn = min(mn, ax)
            }
        }
        if neg % 2 == 0 { return total }
        return total - 2 * mn
    }
}
