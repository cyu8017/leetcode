// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution {
    fun equalSubstring(s: String, t: String, maxCost: Int): Int {
        var left = 0
        var cost = 0
        var answer = 0
        for (right in s.indices) {
            cost += kotlin.math.abs(s[right] - t[right])
            while (cost > maxCost) {
                cost -= kotlin.math.abs(s[left] - t[left])
                left++
            }
            answer = maxOf(answer, right - left + 1)
        }
        return answer
    }
}
