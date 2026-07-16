class Solution {
    func numDistinct(_ s: String, _ t: String) -> Int {
        let source = Array(s)
        let target = Array(t)
        var dp = Array(repeating: 0, count: target.count + 1)
        dp[0] = 1
        for character in source {
            for index in stride(from: target.count - 1, through: 0, by: -1) {
                if character == target[index] {
                    dp[index + 1] += dp[index]
                }
            }
        }
        return dp[target.count]
    }
}