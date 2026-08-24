// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

class Solution {
    func maxIncreasingSubarrays(_ nums: [Int]) -> Int {
        let n = nums.count
        var up = Array(repeating: 1, count: n)
        for i in stride(from: n - 2, through: 0, by: -1) {
            up[i] = nums[i] < nums[i + 1] ? up[i + 1] + 1 : 1
        }
        var lo = 1, hi = n / 2
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(up, n, mid) { lo = mid } else { hi = mid - 1 }
        }
        return lo
    }

    private func ok(_ up: [Int], _ n: Int, _ k: Int) -> Bool {
        if n < 2 * k { return false }
        for i in 0...(n - 2 * k) {
            if up[i] >= k && up[i + k] >= k { return true }
        }
        return false
    }
}
