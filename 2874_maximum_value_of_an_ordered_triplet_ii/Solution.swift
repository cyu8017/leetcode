// LeetCode 2874 - Maximum Value of an Ordered Triplet II
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

class Solution {
    func maximumTripletValue(_ nums: [Int]) -> Int {
        var ans = 0, maxI = 0, maxDiff = 0
        for v in nums {
            ans = max(ans, maxDiff * v)
            maxDiff = max(maxDiff, maxI - v)
            maxI = max(maxI, v)
        }
        return ans
    }
}
