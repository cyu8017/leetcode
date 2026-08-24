// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

class Solution {
    func optimalDivision(_ nums: [Int]) -> String {
        if nums.count == 1 { return String(nums[0]) }
        if nums.count == 2 { return "\(nums[0])/\(nums[1])" }
        var result = "\(nums[0])/("
        for i in 1..<nums.count {
            if i > 1 { result += "/" }
            result += String(nums[i])
        }
        result += ")"
        return result
    }
}
