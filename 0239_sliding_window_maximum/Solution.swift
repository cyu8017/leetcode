// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

class Solution {
    func maxSlidingWindow(_ nums: [Int], _ k: Int) -> [Int] {
        var window: [Int] = []
        var result: [Int] = []

        for index in 0..<nums.count {
            while !window.isEmpty && nums[window[window.count - 1]] <= nums[index] {
                window.removeLast()
            }
            window.append(index)
            if window[0] <= index - k {
                window.removeFirst()
            }
            if index >= k - 1 {
                result.append(nums[window[0]])
            }
        }

        return result
    }
}
