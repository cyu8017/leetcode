// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

class Solution {
    func minCost(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var cnt2 = [Int: Int]()
        for x in nums2 { cnt2[x, default: 0] += 1 }
        var cnt1 = [Int: Int]()
        for x in nums1 {
            if let c = cnt2[x], c > 0 { cnt2[x] = c - 1 }
            else { cnt1[x, default: 0] += 1 }
        }
        var ans = 0
        for v in cnt1.values {
            if v % 2 == 1 { return -1 }
            ans += v / 2
        }
        for v in cnt2.values {
            if v % 2 == 1 { return -1 }
        }
        return ans
    }
}
