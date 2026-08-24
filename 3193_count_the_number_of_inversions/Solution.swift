// LeetCode 3193 - Count the Number of Inversions
// https://leetcode.com/problems/count-the-number-of-inversions/

class Solution {
    func numberOfPermutations(_ n: Int, _ requirements: [[Int]]) -> Int {
        var req = Array(repeating: -1, count: n)
        for r in requirements { req[r[0]] = r[1] }
        if req[0] > 0 { return 0 }
        req[0] = 0
        let m = req.max()!
        let mod = 1_000_000_007
        var f = Array(repeating: Array(repeating: 0, count: m + 1), count: n)
        f[0][0] = 1
        for i in 1..<n {
            var l = 0, r = m
            if req[i] >= 0 { l = req[i]; r = req[i] }
            if l <= r {
                for j in l...r {
                    for k in 0...min(i, j) {
                        f[i][j] = (f[i][j] + f[i - 1][j - k]) % mod
                    }
                }
            }
        }
        return f[n - 1][req[n - 1]]
    }
}
