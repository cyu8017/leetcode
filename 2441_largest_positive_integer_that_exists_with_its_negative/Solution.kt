// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

import java.util.HashSet

class Solution {
    fun findMaxK(nums: IntArray): Int {
            var seen = HashSet()
            var ans: Int = -1
            for (x in nums) {
                seen.add(x)
                if (x > 0 && seen.contains(-x) && x > ans) ans = x
                if (x < 0 && seen.contains(-x) && -x > ans) ans = -x
            }
            return ans
    }
}
