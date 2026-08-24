// LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

class Solution {
    func longestAlternating(_ nums: [Int]) -> Int {
        let n = nums.count
        var l1 = [Int](repeating: 1, count: n)
        var l2 = [Int](repeating: 1, count: n)
        var r1 = [Int](repeating: 1, count: n)
        var r2 = [Int](repeating: 1, count: n)
        var ans = 0
        if n > 1 {
            for i in 1..<n {
                if nums[i - 1] < nums[i] { l1[i] = l2[i - 1] + 1 }
                else if nums[i - 1] > nums[i] { l2[i] = l1[i - 1] + 1 }
                ans = max(ans, max(l1[i], l2[i]))
            }
            for i in stride(from: n - 2, through: 0, by: -1) {
                if nums[i + 1] > nums[i] { r1[i] = r2[i + 1] + 1 }
                else if nums[i + 1] < nums[i] { r2[i] = r1[i + 1] + 1 }
            }
        }
        if n > 2 {
            for i in 1..<(n - 1) {
                if nums[i - 1] < nums[i + 1] { ans = max(ans, l2[i - 1] + r2[i + 1]) }
                else if nums[i - 1] > nums[i + 1] { ans = max(ans, l1[i - 1] + r1[i + 1]) }
            }
        }
        return ans
    }
}
