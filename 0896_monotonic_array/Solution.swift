// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

class Solution {
    func isMonotonic(_ nums: [Int]) -> Bool {
        var inc = true, dec = true
        for i in 1..<nums.count {
            if nums[i] < nums[i - 1] { inc = false }
            if nums[i] > nums[i - 1] { dec = false }
        }
        return inc || dec
    }
}
