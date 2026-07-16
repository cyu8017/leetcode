// LeetCode 0454 - 4Sum II
// https://leetcode.com/problems/4sum-ii/

class Solution {
    func fourSumCount(_ nums1: [Int], _ nums2: [Int], _ nums3: [Int], _ nums4: [Int]) -> Int {
        var pairSums: [Int: Int] = [:]
        for a in nums1 {
            for b in nums2 {
                let sum = a + b
                pairSums[sum, default: 0] += 1
            }
        }

        var total = 0
        for c in nums3 {
            for d in nums4 {
                total += pairSums[-(c + d), default: 0]
            }
        }
        return total
    }
}
