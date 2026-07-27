// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

class Solution {
    func restoreMatrix(_ rowSum: [Int], _ colSum: [Int]) -> [[Int]] {
        var rowSum = rowSum
        var colSum = colSum
        var ans = [[Int]](repeating: [Int](repeating: 0, count: colSum.count), count: rowSum.count)
        var i = 0, j = 0
        while i < rowSum.count && j < colSum.count {
            let x = min(rowSum[i], colSum[j])
            ans[i][j] = x
            rowSum[i] -= x
            colSum[j] -= x
            if rowSum[i] == 0 { i += 1 }
            if colSum[j] == 0 { j += 1 }
        }
        return ans
    }
}
