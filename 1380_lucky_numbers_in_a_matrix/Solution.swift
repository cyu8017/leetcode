// LeetCode 1380 - Lucky Numbers in a Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution {
    func luckyNumbers (_ matrix: [[Int]]) -> [Int] {
        let mins = Set(matrix.map { $0.min()! })
        var maxs = Set<Int>()
        for c in 0..<matrix[0].count {
            maxs.insert((0..<matrix.count).map { matrix[$0][c] }.max()!)
        }
        return Array(mins.intersection(maxs))
    }
}
