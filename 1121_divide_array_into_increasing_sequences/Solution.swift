// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

class Solution {
    func canDivideIntoSubsequences(_ nums: [Int], _ k: Int) -> Bool {
        var count: [Int: Int] = [:]
        var mx = 0
        for x in nums {
            count[x, default: 0] += 1
            mx = max(mx, count[x]!)
        }
        return nums.count >= k * mx
    }
}
