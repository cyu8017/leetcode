// LeetCode 1428 - Leftmost Column with at Least a One
// https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *     func get(_ row: Int, _ col: Int) -> Int {}
 *     func dimensions() -> [Int] {}
 * }
 */
class Solution {
    func leftMostColumnWithOne(_ binaryMatrix: BinaryMatrix) -> Int {
        let dim = binaryMatrix.dimensions()
        let rows = dim[0], cols = dim[1]
        var row = 0, col = cols - 1, answer = -1
        while row < rows && col >= 0 {
            if binaryMatrix.get(row, col) == 1 {
                answer = col
                col -= 1
            } else {
                row += 1
            }
        }
        return answer
    }
}
