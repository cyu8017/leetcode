// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

class Solution {
    func zigZagArrays(_ n: Int, _ l: Int, _ r: Int) -> Int {
        let MOD = 1_000_000_007
        let m = r - l + 1
        if n == 1 { return m % MOD }
        var up = Array(repeating: 1, count: m)
        var down = Array(repeating: 1, count: m)
        if n >= 2 {
            for _ in 2...n {
                var pref = Array(repeating: 0, count: m + 1)
                for j in 0..<m { pref[j + 1] = (pref[j] + down[j]) % MOD }
                var nup = Array(repeating: 0, count: m)
                for j in 0..<m { nup[j] = pref[j] }
                var suf = Array(repeating: 0, count: m + 1)
                for j in stride(from: m - 1, through: 0, by: -1) { suf[j] = (suf[j + 1] + up[j]) % MOD }
                var ndown = Array(repeating: 0, count: m)
                for j in 0..<m { ndown[j] = suf[j + 1] }
                up = nup
                down = ndown
            }
        }
        var ans = 0
        for j in 0..<m {
            ans = (ans + up[j]) % MOD
            ans = (ans + down[j]) % MOD
        }
        return ans
    }
}
