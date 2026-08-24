// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

class Solution {
    fun countCompleteDayPairs(hours: IntArray): Int {
        var cnt = IntArray(24)
        var ans = 0
        for (x in hours) {
            ans += cnt[(24 - x % 24) % 24]
            cnt[x % 24]++
        }
        return ans
    }
}
