// LeetCode 0410 - Split Array Largest Sum
// https://leetcode.com/problems/split-array-largest-sum/

class Solution {
    func splitArray(_ nums: [Int], _ k: Int) -> Int {
        var left = nums.max() ?? 0
        var right = nums.reduce(0, +)

        while left < right {
            let mid = (left + right) / 2
            if canSplit(nums, k, mid) {
                right = mid
            } else {
                left = mid + 1
            }
        }

        return left
    }

    private func canSplit(_ nums: [Int], _ k: Int, _ limit: Int) -> Bool {
        var parts = 1
        var current = 0
        for value in nums {
            if current + value > limit {
                parts += 1
                current = 0
            }
            current += value
        }
        return parts <= k
    }
}
