// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

class Solution {
    func beautifulPartitions(_ s: String, _ k: Int, _ minLength: Int) -> Int {
        func isPrime(_ c: Character) -> Bool {
            c == "2" || c == "3" || c == "5" || c == "7"
        }
        let chars = Array(s)
        let n = chars.count
        let mod = 1_000_000_007
        if !isPrime(chars[0]) || isPrime(chars[n - 1]) { return 0 }
        var dp = [[Int]](repeating: [Int](repeating: 0, count: n + 1), count: k + 1)
        dp[0][0] = 1
        for p in 1...k {
            var pref = 0, j = 0
            for i in 1...n {
                while j <= i - minLength {
                    if j == 0 || (isPrime(chars[j]) && !isPrime(chars[j - 1])) {
                        pref = (pref + dp[p - 1][j]) % mod
                    }
                    j += 1
                }
                if !isPrime(chars[i - 1]) { dp[p][i] = pref }
            }
        }
        return dp[k][n]
    }
}
