// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

class Solution {
    func minimumWhiteTiles(_ floor: String, _ numCarpets: Int, _ carpetLen: Int) -> Int {
        let s = Array(floor)
        let n = s.count
        let inf = 1 << 30
        var dp = [[Int]](repeating: [Int](repeating: inf, count: n + 1), count: numCarpets + 1)
        dp[0][0] = 0
        for j in 1...n {
            dp[0][j] = dp[0][j - 1] + (s[j - 1] == "1" ? 1 : 0)
        }
        if numCarpets == 0 { return dp[0][n] }
        for c in 1...numCarpets {
            dp[c][0] = 0
            for j in 1...n {
                dp[c][j] = dp[c][j - 1] + (s[j - 1] == "1" ? 1 : 0)
                let start = max(0, j - carpetLen)
                dp[c][j] = min(dp[c][j], dp[c - 1][start])
            }
        }
        return dp[numCarpets][n]
    }
}
