// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

class Solution {
    func maxValueAfterReverse(_ nums: [Int]) -> Int {
        var base = 0
        for i in 0..<(nums.count - 1) { base += abs(nums[i] - nums[i + 1]) }
        var gain = 0, low = Int.max / 4, high = Int.min / 4
        for i in 0..<(nums.count - 1) {
            let a = nums[i], b = nums[i + 1]
            gain = max(gain, abs(nums[0] - b) - abs(a - b), abs(nums[nums.count - 1] - a) - abs(a - b))
            low = min(low, max(a, b))
            high = max(high, min(a, b))
        }
        return base + max(gain, 2 * (high - low))
    }
}
