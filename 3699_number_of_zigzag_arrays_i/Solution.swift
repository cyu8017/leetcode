// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

class Solution {
    func zigZagArrays(_ n: Int, _ l: Int, _ r: Int) -> Int {
        let MOD = 1_000_000_007
        let m = r - l + 1
        if n == 1 { return m % MOD }
        var up = Array(repeating: 1, count: m)
        var down = Array(repeating: 1, count: m)
        if n >= 2 {
            for _ in 2...n {
                var prefDown = Array(repeating: 0, count: m + 1)
                for j in 0..<m { prefDown[j + 1] = (prefDown[j] + down[j]) % MOD }
                var nup = Array(repeating: 0, count: m)
                for j in 0..<m { nup[j] = prefDown[j] }
                var sufUp = Array(repeating: 0, count: m + 1)
                for j in stride(from: m - 1, through: 0, by: -1) { sufUp[j] = (sufUp[j + 1] + up[j]) % MOD }
                var ndown = Array(repeating: 0, count: m)
                for j in 0..<m { ndown[j] = sufUp[j + 1] }
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
