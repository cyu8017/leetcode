// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var g: [Int] = []
        for x in nums {
            var l = 0, r = g.count
            while l < r {
                let mid = (l + r) >> 1
                if g[mid] < x { r = mid }
                else { l = mid + 1 }
            }
            if l == g.count { g.append(x) }
            else { g[l] = x }
        }
        return g.count
    }
}
