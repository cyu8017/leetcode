// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

class Solution {
    func maxValue(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let MAX = 128
        var left = Array(repeating: Array(repeating: Array(repeating: false, count: MAX), count: k + 1), count: n + 1)
        left[0][0][0] = true
        for i in 0..<n {
            for j in 0...k {
                for v in 0..<MAX {
                    if !left[i][j][v] { continue }
                    left[i + 1][j][v] = true
                    if j < k { left[i + 1][j + 1][v | nums[i]] = true }
                }
            }
        }
        var right = Array(repeating: Array(repeating: Array(repeating: false, count: MAX), count: k + 1), count: n + 1)
        right[n][0][0] = true
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in 0...k {
                for v in 0..<MAX {
                    if !right[i + 1][j][v] { continue }
                    right[i][j][v] = true
                    if j < k { right[i][j + 1][v | nums[i]] = true }
                }
            }
        }
        var ans = 0
        if 2 * k <= n {
            for mid in k...(n - k) {
                for a in 0..<MAX {
                    if !left[mid][k][a] { continue }
                    for b in 0..<MAX {
                        if right[mid][k][b] && (a ^ b) > ans { ans = a ^ b }
                    }
                }
            }
        }
        return ans
    }
}
