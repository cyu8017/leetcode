// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int) -> Int {
        let sorted = nums.sorted()
        var left = 0
        var windowSum = 0
        var best = 0
        for right in 0..<sorted.count {
            let value = sorted[right]
            windowSum += value
            while value * (right - left + 1) - windowSum > k {
                windowSum -= sorted[left]
                left += 1
            }
            best = max(best, right - left + 1)
        }
        return best
    }
}
