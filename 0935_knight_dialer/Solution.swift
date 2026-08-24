// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

class Solution {
    func knightDialer(_ n: Int) -> Int {
        let mod = 1_000_000_007
        let moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        var dp = Array(repeating: 1, count: 10)
        if n > 1 {
            for _ in 0..<(n - 1) {
                var ndp = Array(repeating: 0, count: 10)
                for i in 0..<10 {
                    for j in moves[i] { ndp[j] = (ndp[j] + dp[i]) % mod }
                }
                dp = ndp
            }
        }
        return dp.reduce(0, +) % mod
    }
}
