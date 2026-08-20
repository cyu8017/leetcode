// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution {
    func maxSumDivThree(_ nums: [Int]) -> Int {
        var dp = [0, Int.min / 4, Int.min / 4]
        for x in nums {
            var next = dp
            for s in dp {
                let ns = s + x
                next[ns % 3] = max(next[ns % 3], ns)
            }
            dp = next
        }
        return dp[0]
    }
}
