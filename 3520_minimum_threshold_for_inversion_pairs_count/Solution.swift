// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

class Solution {
    func upperBound(_ a: [Int], _ target: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] <= target { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }

    func countInv(_ nums: [Int], _ k: Int, _ threshold: Int) -> Bool {
        var sorted = [Int]()
        var inv = 0
        for num in nums {
            let left = upperBound(sorted, num)
            let right = upperBound(sorted, num + threshold)
            inv += right - left
            let pos = upperBound(sorted, num)
            sorted.insert(num, at: pos)
        }
        return inv >= k
    }

    func minThreshold(_ nums: [Int], _ k: Int) -> Int {
        var mx = 0
        for v in nums { mx = max(mx, v) }
        var l = 0, r = mx + 1
        while l < r {
            let m = (l + r) / 2
            if countInv(nums, k, m) { r = m } else { l = m + 1 }
        }
        return l > mx ? -1 : l
    }
}
