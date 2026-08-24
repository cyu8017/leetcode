// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

class Solution {
    private var ans = 0
    private var used: [Bool] = []
    private var n = 0

    func selfDivisiblePermutationCount(_ n: Int) -> Int {
        self.n = n
        ans = 0
        used = Array(repeating: false, count: n + 1)
        dfs(1)
        return ans
    }

    private func dfs(_ pos: Int) {
        if pos > n {
            ans += 1
            return
        }
        for v in 1...n {
            if used[v] { continue }
            if gcd(v, pos) != 1 { continue }
            used[v] = true
            dfs(pos + 1)
            used[v] = false
        }
    }

    private func gcd(_ a0: Int, _ b0: Int) -> Int {
        var a = a0, b = b0
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }
}
