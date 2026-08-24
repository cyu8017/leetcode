// LeetCode 2022 - Convert 1D Array Into 2D Array
// https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution {
    func construct2DArray(_ original: [Int], _ m: Int, _ n: Int) -> [[Int]] {
        if original.count != m * n { return [] }
        var ans = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        for i in 0..<m {
            for j in 0..<n { ans[i][j] = original[i * n + j] }
        }
        return ans
    }
}
