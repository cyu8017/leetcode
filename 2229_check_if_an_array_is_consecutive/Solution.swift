// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

class Solution {
    func isConsecutive(_ nums: [Int]) -> Bool {
        var seen = Set<Int>()
        var mn = nums[0], mx = nums[0]
        for x in nums {
            if !seen.insert(x).inserted { return false }
            mn = min(mn, x)
            mx = max(mx, x)
        }
        return mx - mn + 1 == nums.count
    }
}
