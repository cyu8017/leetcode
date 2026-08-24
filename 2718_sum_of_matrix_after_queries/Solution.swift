// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

class Solution {
    func matrixSumQueries(_ n: Int, _ queries: [[Int]]) -> Int {
        var rowDone = Array(repeating: false, count: n)
        var colDone = Array(repeating: false, count: n)
        var rowsLeft = n, colsLeft = n
        var ans = 0
        for i in stride(from: queries.count - 1, through: 0, by: -1) {
            let type = queries[i][0], idx = queries[i][1], val = queries[i][2]
            if type == 0 {
                if !rowDone[idx] {
                    ans += val * colsLeft
                    rowDone[idx] = true
                    rowsLeft -= 1
                }
            } else if !colDone[idx] {
                ans += val * rowsLeft
                colDone[idx] = true
                colsLeft -= 1
            }
        }
        return ans
    }
}
