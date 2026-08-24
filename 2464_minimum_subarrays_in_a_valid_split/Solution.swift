// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

class Solution {
    func validSubarraySplit(_ nums: [Int]) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        let n = nums.count
        let INF = 1 << 30
        var dp = [Int](repeating: INF, count: n + 1)
        dp[0] = 0
        for i in 0..<n {
            if dp[i] >= INF { continue }
            for j in i..<n {
                if gcd(nums[i], nums[j]) > 1 {
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)
                }
            }
        }
        return dp[n] >= INF ? -1 : dp[n]
    }
}
