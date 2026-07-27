// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

class Solution {
    func maximumUniqueSubarray(_ nums: [Int]) -> Int {
        var seen = [Int: Int]()
        var left = 0, cur = 0, best = 0
        for right in 0..<nums.count {
            let x = nums[right]
            if let stop = seen[x], stop >= left {
                while left <= stop {
                    cur -= nums[left]
                    left += 1
                }
            }
            seen[x] = right
            cur += x
            best = max(best, cur)
        }
        return best
    }
}
