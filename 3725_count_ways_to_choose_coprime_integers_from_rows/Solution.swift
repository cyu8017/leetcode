// LeetCode 3725 - Count Ways To Choose Coprime Integers From Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

class Solution {
    func countCoprime(_ mat: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        let m = mat.count
        var dp = [Int: Int]()
        for v in mat[0] { dp[v, default: 0] += 1 }
        if m > 1 {
            for i in 1..<m {
                var ndp = [Int: Int]()
                for v in mat[i] {
                    for (key, val) in dp {
                        let ng = gcd(key, v)
                        ndp[ng, default: 0] = (ndp[ng, default: 0] + val) % MOD
                    }
                }
                dp = ndp
            }
        }
        return dp[1, default: 0]
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a, b = b
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }
}
