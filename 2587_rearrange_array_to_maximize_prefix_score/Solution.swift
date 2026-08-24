// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        var sum = 0, ans = 0
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            sum += nums[i]
            if sum > 0 { ans += 1 } else { break }
        }
        return ans
    }
}
