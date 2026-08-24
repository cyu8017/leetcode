// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

class Solution {
    func kthSmallestProduct(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        var lo = -10_000_000_000, hi = 10_000_000_000
        while lo < hi {
            let mid = lo + (hi - lo) / 2
            if countLE(nums1, nums2, mid) >= k { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func countLE(_ nums1: [Int], _ nums2: [Int], _ x: Int) -> Int {
        var cnt = 0
        for a in nums1 {
            if a > 0 {
                var lo = 0, hi = nums2.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if a * nums2[mid] <= x { lo = mid + 1 }
                    else { hi = mid }
                }
                cnt += lo
            } else if a < 0 {
                var lo = 0, hi = nums2.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if a * nums2[mid] <= x { hi = mid }
                    else { lo = mid + 1 }
                }
                cnt += nums2.count - lo
            } else if x >= 0 {
                cnt += nums2.count
            }
        }
        return cnt
    }
}
