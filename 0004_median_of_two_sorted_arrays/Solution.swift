// LeetCode 0004 - Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution {
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        var a = nums1
        var b = nums2
        if a.count > b.count {
            swap(&a, &b)
        }

        let m = a.count
        let n = b.count
        let totalLeft = (m + n + 1) / 2
        var lo = 0
        var hi = m

        while lo <= hi {
            let i = (lo + hi) / 2
            let j = totalLeft - i

            let nums1LeftMax = i == 0 ? Int.min : a[i - 1]
            let nums1RightMin = i == m ? Int.max : a[i]
            let nums2LeftMax = j == 0 ? Int.min : b[j - 1]
            let nums2RightMin = j == n ? Int.max : b[j]

            if nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin {
                if (m + n) % 2 == 1 {
                    return Double(max(nums1LeftMax, nums2LeftMax))
                }
                return Double(max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2.0
            }

            if nums1LeftMax > nums2RightMin {
                hi = i - 1
            } else {
                lo = i + 1
            }
        }

        return 0.0
    }
}
