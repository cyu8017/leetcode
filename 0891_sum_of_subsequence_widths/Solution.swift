// LeetCode 0891 - Sum of Subsequence Widths
// https://leetcode.com/problems/sum-of-subsequence-widths/

class Solution {
    func sumSubseqWidths(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let a = nums.sorted()
        let n = a.count
        var pow2 = Array(repeating: 1, count: n)
        if n > 1 {
            for i in 1..<n { pow2[i] = (pow2[i - 1] * 2) % mod }
        }
        var ans = 0
        for i in 0..<n {
            ans = (ans + a[i] * ((pow2[i] - pow2[n - 1 - i] + mod) % mod)) % mod
        }
        return (ans + mod) % mod
    }
}
