// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

class Solution {
    func summaryRanges(_ nums: [Int]) -> [String] {
        var result: [String] = []
        var index = 0

        while index < nums.count {
            let start = nums[index]
            while index + 1 < nums.count && nums[index + 1] == nums[index] + 1 {
                index += 1
            }
            if start == nums[index] {
                result.append(String(start))
            } else {
                result.append("\(start)->\(nums[index])")
            }
            index += 1
        }

        return result
    }
}
