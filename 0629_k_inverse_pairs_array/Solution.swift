// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/

class Solution {
    func kInversePairs(_ n: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        var dp = Array(repeating: 0, count: k + 1)
        dp[0] = 1
        for size in 1...n {
            var nxt = Array(repeating: 0, count: k + 1)
            var prefix = 0
            for pairs in 0...k {
                prefix = (prefix + dp[pairs]) % mod
                if pairs >= size {
                    prefix = (prefix - dp[pairs - size] + mod) % mod
                }
                nxt[pairs] = prefix
            }
            dp = nxt
        }
        return dp[k]
    }
}
