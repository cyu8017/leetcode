// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

class Solution {
    func minAbsoluteSumDiff(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let mod = 1_000_000_007
        let sortedNums1 = nums1.sorted()
        var total = 0
        for i in 0..<nums1.count {
            total += abs(nums1[i] - nums2[i])
        }
        var bestGain = 0
        for i in 0..<nums2.count {
            let target = nums2[i]
            let current = abs(nums1[i] - target)
            var lo = 0, hi = sortedNums1.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if sortedNums1[mid] < target { lo = mid + 1 } else { hi = mid }
            }
            for j in [lo - 1, lo] where j >= 0 && j < sortedNums1.count {
                bestGain = max(bestGain, current - abs(sortedNums1[j] - target))
            }
        }
        return (total - bestGain) % mod
    }
}
