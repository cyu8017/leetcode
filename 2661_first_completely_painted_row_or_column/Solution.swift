// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution {
    func firstCompleteIndex(_ arr: [Int], _ mat: [[Int]]) -> Int {
        let m = mat.count, n = mat[0].count
        var posR = Array(repeating: 0, count: m * n + 1)
        var posC = Array(repeating: 0, count: m * n + 1)
        for i in 0..<m {
            for j in 0..<n {
                posR[mat[i][j]] = i
                posC[mat[i][j]] = j
            }
        }
        var rowCnt = Array(repeating: 0, count: m)
        var colCnt = Array(repeating: 0, count: n)
        for i in arr.indices {
            let r = posR[arr[i]], c = posC[arr[i]]
            rowCnt[r] += 1
            colCnt[c] += 1
            if rowCnt[r] == n || colCnt[c] == m { return i }
        }
        return -1
    }
}
