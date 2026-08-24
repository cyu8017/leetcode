// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

import java.util.HashSet

class Solution {
    fun longestSquareStreak(nums: IntArray): Int {
            var set = HashSet()
            for (x in nums) set.add(x)
            var best: Int = -1
            for (x in nums) {
                if (!set.contains(x)) continue
                var length: Int = 0
                var cur: Long = x
                while (set.contains(cur)) {
                    length = length + 1
                    set.remove(cur)
                    if (cur > 100000) break
                    cur = cur * cur
                }
                if (length >= 2 && length > best) best = length
            }
            return best
    }
}
