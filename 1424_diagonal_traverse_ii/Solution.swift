// LeetCode 1424 - Diagonal Traverse II
// https://leetcode.com/problems/diagonal-traverse-ii/

class Solution {
    func findDiagonalOrder(_ nums: [[Int]]) -> [Int] {
        var diagonals = [Int: [Int]]()
        for (row, values) in nums.enumerated() {
            for (col, value) in values.enumerated() {
                diagonals[row + col, default: []].append(value)
            }
        }
        return diagonals.keys.sorted().flatMap { diagonals[$0]!.reversed() }
    }
}
