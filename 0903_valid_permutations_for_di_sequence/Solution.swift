// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

class Solution {
    func numPermsDISequence(_ s: String) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        var dp = Array(repeating: 1, count: n + 1)
        if n >= 1 {
            for i in 1...n {
                var newDp = Array(repeating: 0, count: n + 1)
                if chars[i - 1] == "I" {
                    var postfix = 0
                    for j in stride(from: n - i, through: 0, by: -1) {
                        postfix = (postfix + dp[j + 1]) % mod
                        newDp[j] = postfix
                    }
                } else {
                    var prefix = 0
                    for j in 0...(n - i) {
                        prefix = (prefix + dp[j]) % mod
                        newDp[j] = prefix
                    }
                }
                dp = newDp
            }
        }
        return dp[0]
    }
}
