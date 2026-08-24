// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

class Solution {
    func minSwap(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var swap = Array(repeating: n, count: n)
        var keep = Array(repeating: n, count: n)
        swap[0] = 1
        keep[0] = 0
        for i in 1..<n {
            if nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1] {
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            }
            if nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1] {
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
            }
        }
        return min(swap[n - 1], keep[n - 1])
    }
}
