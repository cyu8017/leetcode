// LeetCode 0213 - House Robber II
// https://leetcode.com/problems/house-robber-ii/

class Solution {
    func rob(_ nums: [Int]) -> Int {
        if nums.count == 1 {
            return nums[0]
        }
        return max(robLinear(Array(nums[0..<nums.count - 1])), robLinear(Array(nums[1...])))
    }

    private func robLinear(_ houses: [Int]) -> Int {
        var prev2 = 0
        var prev1 = 0
        for num in houses {
            let current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        }
        return prev1
    }
}
