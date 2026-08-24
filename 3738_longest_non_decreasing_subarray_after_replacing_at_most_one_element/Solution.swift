// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

class Solution {
    func longestSubarray(_ nums: [Int]) -> Int {
        let n = nums.count
        var left = [Int](repeating: 1, count: n)
        var right = [Int](repeating: 1, count: n)
        if n > 1 {
            for i in 1..<n {
                if nums[i] >= nums[i - 1] { left[i] = left[i - 1] + 1 }
            }
            for i in stride(from: n - 2, through: 0, by: -1) {
                if nums[i] <= nums[i + 1] { right[i] = right[i + 1] + 1 }
            }
        }
        var ans = 0
        for v in left { ans = max(ans, v) }
        for i in 0..<n {
            let a = i > 0 ? left[i - 1] : 0
            let b = i + 1 < n ? right[i + 1] : 0
            if i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1] {
                ans = max(ans, max(a + 1, b + 1))
            } else {
                ans = max(ans, a + b + 1)
            }
        }
        return ans
    }
}
