// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

class Solution {
    func maximumsSplicedArray(_ nums1: [Int], _ nums2: [Int]) -> Int {
        func kadane(_ a: [Int], _ b: [Int]) -> Int {
            var best = 0, cur = 0, sum = 0
            for i in 0..<a.count {
                sum += a[i]
                cur += b[i] - a[i]
                if cur < 0 { cur = 0 }
                best = max(best, cur)
            }
            return sum + best
        }
        return max(kadane(nums1, nums2), kadane(nums2, nums1))
    }
}
