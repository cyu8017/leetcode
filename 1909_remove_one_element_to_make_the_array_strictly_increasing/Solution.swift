// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution {
    func canBeIncreasing(_ nums: [Int]) -> Bool {
        func check(_ skip: Int) -> Bool {
            var prev: Int? = nil
            for (i, x) in nums.enumerated() {
                if i == skip { continue }
                if let p = prev, x <= p { return false }
                prev = x
            }
            return true
        }
        for i in 1..<nums.count {
            if nums[i] <= nums[i - 1] {
                return check(i - 1) || check(i)
            }
        }
        return true
    }
}
