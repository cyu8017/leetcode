// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

class Solution {
    func upperBound(_ nums: [Int], _ target: Int) -> Int {
        var lo = 0, hi = nums.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if nums[mid] <= target { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
