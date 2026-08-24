// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

class Solution {
    func maxCollectedFruits(_ fruits: [[Int]]) -> Int {
        var fruits = fruits
        let n = fruits.count
        var ans = 0
        for i in 0..<n {
            ans += fruits[i][i]
            fruits[i][i] = 0
        }
        let neg = -(1 << 30)
        var dp2 = Array(repeating: Array(repeating: neg, count: n), count: n)
        var dp3 = Array(repeating: Array(repeating: neg, count: n), count: n)
        dp2[0][n - 1] = fruits[0][n - 1]
        for i in 0..<n {
            for j in 0..<n {
                if dp2[i][j] == neg { continue }
                for dj in [-1, 0, 1] {
                    let ni = i + 1, nj = j + dj
                    if ni < n && nj >= 0 && nj < n && nj > ni {
                        let v = dp2[i][j] + fruits[ni][nj]
                        if v > dp2[ni][nj] { dp2[ni][nj] = v }
                    }
                }
            }
        }
        dp3[n - 1][0] = fruits[n - 1][0]
        for j in 0..<n {
            for i in 0..<n {
                if dp3[i][j] == neg { continue }
                for di in [-1, 0, 1] {
                    let ni = i + di, nj = j + 1
                    if ni >= 0 && ni < n && nj < n && ni > nj {
                        let v = dp3[i][j] + fruits[ni][nj]
                        if v > dp3[ni][nj] { dp3[ni][nj] = v }
                    }
                }
            }
        }
        ans += dp2[n - 1][n - 1] + dp3[n - 1][n - 1]
        return ans
    }
}
