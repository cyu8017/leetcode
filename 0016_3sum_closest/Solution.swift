// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

class Solution {
    func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
        let sorted = nums.sorted()
        var closest = sorted[0] + sorted[1] + sorted[2]

        for i in 0..<(sorted.count - 2) {
            var left = i + 1
            var right = sorted.count - 1
            while left < right {
                let total = sorted[i] + sorted[left] + sorted[right]
                if abs(total - target) < abs(closest - target) {
                    closest = total
                }
                if total < target {
                    left += 1
                } else if total > target {
                    right -= 1
                } else {
                    return total
                }
            }
        }

        return closest
    }
}
