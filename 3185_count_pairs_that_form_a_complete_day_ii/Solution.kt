// LeetCode 3185 - Count Pairs That Form a Complete Day II
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

class Solution {
    fun countCompleteDayPairs(hours: IntArray): Long {
        var cnt = IntArray(24)
        var ans = 0
        for (x in hours) {
            ans += cnt[(24 - x % 24) % 24]
            cnt[x % 24]++
        }
        return ans
    }
}
