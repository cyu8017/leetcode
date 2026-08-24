// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

class Solution {
    func sumIndicesWithKSetBits(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        for i in 0..<nums.count {
            if i.nonzeroBitCount == k { ans += nums[i] }
        }
        return ans
    }
}
