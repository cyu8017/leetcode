// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

class Solution {
    func reconstructMatrix(_ upper: Int, _ lower: Int, _ colsum: [Int]) -> [[Int]] {
        var upper = upper, lower = lower
        let n = colsum.count
        var a = [Int](repeating: 0, count: n)
        var b = [Int](repeating: 0, count: n)
        for i in 0..<n where colsum[i] == 2 {
            a[i] = 1; b[i] = 1
            upper -= 1; lower -= 1
        }
        if upper < 0 || lower < 0 { return [] }
        for i in 0..<n where colsum[i] == 1 {
            if upper > 0 { a[i] = 1; upper -= 1 }
            else if lower > 0 { b[i] = 1; lower -= 1 }
            else { return [] }
        }
        return upper == 0 && lower == 0 ? [a, b] : []
    }
}
