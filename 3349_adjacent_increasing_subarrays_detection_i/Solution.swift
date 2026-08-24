// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution {
    func hasIncreasingSubarrays(_ nums: [Int], _ k: Int) -> Bool {
        let n = nums.count
        if n < 2 * k { return false }
        for i in 0...(n - 2 * k) {
            if inc(nums, i, k) && inc(nums, i + k, k) { return true }
        }
        return false
    }

    private func inc(_ nums: [Int], _ start: Int, _ k: Int) -> Bool {
        if k <= 1 { return true }
        for i in start..<(start + k - 1) {
            if nums[i] >= nums[i + 1] { return false }
        }
        return true
    }
}
