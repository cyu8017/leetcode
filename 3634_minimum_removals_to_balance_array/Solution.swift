// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution {
    func minRemoval(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        var cnt = 0
        for i in 0..<n {
            var j = n
            if nums[i] * k <= nums[n - 1] {
                let target = nums[i] * k + 1
                j = lowerBound(nums, target)
            }
            cnt = max(cnt, j - i)
        }
        return n - cnt
    }

    func lowerBound(_ a: [Int], _ target: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < target { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
