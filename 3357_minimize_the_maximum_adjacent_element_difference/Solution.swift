// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

class Solution {
    func minDifference(_ nums: [Int]) -> Int {
        let n = nums.count
        var lo = 0, hi = 1_000_000_000
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(mid, nums, n) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }

    private func ok(_ d: Int, _ nums: [Int], _ n: Int) -> Bool {
        var prev = -1
        var i = 0
        while i < n {
            if nums[i] != -1 {
                if prev != -1 && abs(nums[i] - prev) > d { return false }
                prev = nums[i]
                i += 1
                continue
            }
            var j = i
            while j < n && nums[j] == -1 { j += 1 }
            let left = prev
            let right = j < n ? nums[j] : -1
            let gap = j - i
            if left == -1 && right == -1 { return true }
            if left == -1 || right == -1 {
                prev = -1
                i = j
                continue
            }
            if abs(left - right) > d * (gap + 1) { return false }
            prev = -1
            i = j
        }
        return true
    }
}
