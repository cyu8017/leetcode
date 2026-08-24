// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

class Solution {
    func spiralMatrixIII(_ rows: Int, _ cols: Int, _ rStart: Int, _ cStart: Int) -> [[Int]] {
        var ans = [[rStart, cStart]]
        if rows * cols == 1 { return ans }
        var r = rStart, c = cStart
        let dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        var steps = 1
        while ans.count < rows * cols {
            for d in 0..<4 {
                let dr = dirs[d][0], dc = dirs[d][1]
                for _ in 0..<steps {
                    r += dr
                    c += dc
                    if r >= 0 && r < rows && c >= 0 && c < cols {
                        ans.append([r, c])
                        if ans.count == rows * cols { return ans }
                    }
                }
                if d % 2 == 1 { steps += 1 }
            }
        }
        return ans
    }
}
