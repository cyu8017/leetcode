// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution {
    func oddCells(_ m: Int, _ n: Int, _ indices: [[Int]]) -> Int {
        var rows = [Int](repeating: 0, count: m)
        var cols = [Int](repeating: 0, count: n)
        for idx in indices {
            rows[idx[0]] += 1
            cols[idx[1]] += 1
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n where (rows[i] + cols[j]) % 2 == 1 { ans += 1 }
        }
        return ans
    }
}
