// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

class Solution {
    func numFactoredBinaryTrees(_ arr: [Int]) -> Int {
        let mod = 1_000_000_007
        let nums = arr.sorted()
        var dp = [Int: Int]()
        for i in 0..<nums.count {
            let x = nums[i]
            var ways = 1
            for j in 0..<i {
                let left = nums[j]
                if x % left == 0 {
                    let right = x / left
                    if let wr = dp[right], let wl = dp[left] {
                        ways = (ways + wl * wr) % mod
                    }
                }
            }
            dp[x] = ways
        }
        var ans = 0
        for v in dp.values { ans = (ans + v) % mod }
        return ans
    }
}
