// LeetCode 0198 - House Robber
class Solution {
    func rob(_ nums: [Int]) -> Int {
        var prev2 = 0
        var prev1 = 0
        for num in nums {
            let current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        }
        return prev1
    }
}