// LeetCode 1989
// https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

class Solution {
    fun catchMaximumAmountofPeople(team: IntArray, dist: Int): Int {
        var ans = 0
        var j = 0
        val n = team.size
        for (i in team.indices) {
            if (team[i] != 0) {
                while (j < n && (team[j] != 0 || i - j > dist)) j++
                if (j < n && kotlin.math.abs(i - j) <= dist) {
                    ans++
                    j++
                }
            }
        }
        return ans
    }
}
