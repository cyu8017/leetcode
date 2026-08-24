// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

class Solution {
    func totalSteps(_ nums: [Int]) -> Int {
        var stack: [(Int, Int)] = []
        var ans = 0
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            var steps = 0
            while let last = stack.last, nums[i] > last.0 {
                steps = max(steps, last.1)
                stack.removeLast()
                steps += 1
            }
            ans = max(ans, steps)
            stack.append((nums[i], steps))
        }
        return ans
    }
}
