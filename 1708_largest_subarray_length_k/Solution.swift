// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/

class Solution {
    func largestSubarray(_ nums: [Int], _ k: Int) -> [Int] {
        var start = 0
        var i = 1
        while i + k <= nums.count {
            if nums[i] > nums[start] {
                start = i
            }
            i += 1
        }
        return Array(nums[start..<(start + k)])
    }
}
