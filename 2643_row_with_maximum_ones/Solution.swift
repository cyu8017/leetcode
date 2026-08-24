// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

class Solution {
    func rowAndMaximumOnes(_ mat: [[Int]]) -> [Int] {
        var bestRow = 0
        var bestCnt = -1
        for i in mat.indices {
            let cnt = mat[i].reduce(0, +)
            if cnt > bestCnt {
                bestCnt = cnt
                bestRow = i
            }
        }
        return [bestRow, bestCnt]
    }
}
