// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

class Solution {
    func minCost(_ nums: [Int], _ costs: [Int]) -> Int {
        let n = nums.count
        var dp = [Int](repeating: Int.max / 4, count: n)
        dp[0] = 0
        var stack1: [Int] = []
        var stack2: [Int] = []
        for i in 0..<n {
            while let last = stack1.last, nums[last] <= nums[i] {
                stack1.removeLast()
                dp[i] = min(dp[i], dp[last] + costs[i])
            }
            while let last = stack2.last, nums[last] > nums[i] {
                stack2.removeLast()
                dp[i] = min(dp[i], dp[last] + costs[i])
            }
            if let last = stack1.last { dp[i] = min(dp[i], dp[last] + costs[i]) }
            if let last = stack2.last { dp[i] = min(dp[i], dp[last] + costs[i]) }
            stack1.append(i)
            stack2.append(i)
        }
        return dp[n - 1]
    }
}
