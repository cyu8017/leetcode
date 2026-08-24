// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

class Solution {
    func findMaxAverage(_ nums: [Int], _ k: Int) -> Double {
        var left = Double(nums[0])
        var right = Double(nums[0])
        for num in nums {
            left = min(left, Double(num))
            right = max(right, Double(num))
        }
        for _ in 0..<80 {
            let mid = (left + right) / 2.0
            if canReach(nums, k, mid) { left = mid } else { right = mid }
        }
        return left
    }

    private func canReach(_ nums: [Int], _ k: Int, _ mid: Double) -> Bool {
        var prefix = 0.0
        for i in 0..<k { prefix += Double(nums[i]) - mid }
        if prefix >= 0 { return true }
        var prev = 0.0
        var minPrev = 0.0
        if k < nums.count {
            for i in k..<nums.count {
                prefix += Double(nums[i]) - mid
                prev += Double(nums[i - k]) - mid
                minPrev = min(minPrev, prev)
                if prefix - minPrev >= 0 { return true }
            }
        }
        return false
    }
}
