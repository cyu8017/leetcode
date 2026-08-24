// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

class Solution {
    func longestSquareStreak(_ nums: [Int]) -> Int {
        var set = Set(nums.map { Int64($0) })
        var best = -1
        for x in nums {
            var length = 0
            var cur = Int64(x)
            while set.contains(cur) {
                length += 1
                set.remove(cur)
                if cur > 100000 { break }
                cur = cur * cur
            }
            if length >= 2 { best = max(best, length) }
        }
        return best
    }
}
