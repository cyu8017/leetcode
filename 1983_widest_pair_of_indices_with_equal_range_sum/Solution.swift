// LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
// https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

class Solution {
    func widestPairOfIndices(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var first: [Int: Int] = [0: -1]
        var ans = 0, s = 0
        for i in 0..<nums1.count {
            s += nums1[i] - nums2[i]
            if let f = first[s] {
                ans = max(ans, i - f)
            } else {
                first[s] = i
            }
        }
        return ans
    }
}
