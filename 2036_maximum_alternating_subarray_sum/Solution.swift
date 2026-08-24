// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

class Solution {
    func maximumAlternatingSubarraySum(_ nums: [Int]) -> Int {
        var pos = nums[0]
        var neg: Int? = nil
        var ans = nums[0]
        for i in 1..<nums.count {
            let x = nums[i]
            let newPos = neg == nil ? x : max(x, neg! + x)
            let newNeg = pos - x
            ans = max(ans, newPos, newNeg)
            pos = newPos
            neg = newNeg
        }
        return ans
    }
}
