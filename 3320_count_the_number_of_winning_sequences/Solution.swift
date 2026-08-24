// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

class Solution {
    func countWinningSequences(_ s: String) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        var mp = [Character: Int]()
        mp["F"] = 0; mp["W"] = 1; mp["E"] = 2
        let beat = [2, 0, 1]
        var score = Array(repeating: Array(repeating: 0, count: 3), count: 3)
        for a in 0..<3 {
            for b in 0..<3 {
                if a == b { score[a][b] = 0 }
                else if beat[a] == b { score[a][b] = 1 }
                else { score[a][b] = -1 }
            }
        }
        let offset = n
        var dp = Array(repeating: Array(repeating: 0, count: 2 * n + 1), count: 3)
        let b0 = mp[chars[0]]!
        for a in 0..<3 { dp[a][score[a][b0] + offset] = 1 }
        if n > 1 {
            for i in 1..<n {
                var ndp = Array(repeating: Array(repeating: 0, count: 2 * n + 1), count: 3)
                let b = mp[chars[i]]!
                for last in 0..<3 {
                    for d in 0...(2 * n) {
                        if dp[last][d] == 0 { continue }
                        for a in 0..<3 where a != last {
                            let nd = d + score[a][b]
                            if nd < 0 || nd > 2 * n { continue }
                            ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod
                        }
                    }
                }
                dp = ndp
            }
        }
        var ans = 0
        for a in 0..<3 {
            if offset + 1 <= 2 * n {
                for d in (offset + 1)...(2 * n) { ans = (ans + dp[a][d]) % mod }
            }
        }
        return ans
    }
}
