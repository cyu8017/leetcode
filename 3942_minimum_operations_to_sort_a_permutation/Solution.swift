// LeetCode 3942 - Minimum Operations to Sort a Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/


class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        var zero = 0
        for i in 0..<n {
            if nums[i] == 0 { zero = i; break }
        }
        var ans = Int.max
        if check(nums, zero, 1) {
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)
        }
        if check(nums, zero, -1) {
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)
        }
        return ans == Int.max ? -1 : ans
    }

    private func check(_ nums: [Int], _ zero: Int, _ step: Int) -> Bool {
        let n = nums.count
        for i in 1..<n {
            let prev = ((zero + (i - 1) * step) % n + n) % n
            let curr = ((zero + i * step) % n + n) % n
            if nums[prev] > nums[curr] { return false }
        }
        return true
    }
}
