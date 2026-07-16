// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

class Solution {
    func threeSumSmaller(_ nums: [Int], _ target: Int) -> Int {
        let sorted = nums.sorted()
        var count = 0
        for index in 0..<(sorted.count - 2) {
            var left = index + 1
            var right = sorted.count - 1
            while left < right {
                let total = sorted[index] + sorted[left] + sorted[right]
                if total < target {
                    count += right - left
                    left += 1
                } else {
                    right -= 1
                }
            }
        }
        return count
    }
}
