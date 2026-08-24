// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/

class Solution {
    func arrayNesting(_ nums: [Int]) -> Int {
        var nums = nums
        var best = 0
        for i in 0..<nums.count {
            if nums[i] < 0 { continue }
            var length = 0
            var j = i
            while nums[j] >= 0 {
                let nxt = nums[j]
                nums[j] = -1
                j = nxt
                length += 1
            }
            best = max(best, length)
        }
        return best
    }
}
