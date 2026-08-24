// LeetCode 0643 - Maximum Average Subarray I
// https://leetcode.com/problems/maximum-average-subarray-i/

class Solution {
    func findMaxAverage(_ nums: [Int], _ k: Int) -> Double {
        var window = 0
        for i in 0..<k { window += nums[i] }
        var best = window
        if k < nums.count {
            for i in k..<nums.count {
                window += nums[i] - nums[i - k]
                best = max(best, window)
            }
        }
        return Double(best) / Double(k)
    }
}
