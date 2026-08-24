// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

class Solution {
    func minimumIncrements(_ nums: [Int], _ target: [Int]) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        func lcm(_ a: Int, _ b: Int) -> Int { return a / gcd(a, b) * b }
        let m = target.count
        let N = 1 << m
        let inf = Int(1e18)
        var dp = Array(repeating: inf, count: N)
        dp[0] = 0
        for x in nums {
            var ndp = dp
            for mask in 0..<N {
                for sub in 1..<N {
                    var L = 1
                    var ok = true
                    for i in 0..<m where (sub & (1 << i)) != 0 {
                        L = lcm(L, target[i])
                        if L > 1_000_000_000 { ok = false; break }
                    }
                    if !ok { continue }
                    let cost = (L - x % L) % L
                    let nmask = mask | sub
                    if dp[mask] + cost < ndp[nmask] { ndp[nmask] = dp[mask] + cost }
                }
            }
            dp = ndp
        }
        return dp[N - 1]
    }
}
