// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution {

    private fun toMin(t: String): Int {

            return (t[0] - '0') * 600 + (t[1] - '0') * 60
                    + (t[3] - '0') * 10 + (t[4] - '0')

    }


    fun convertTime(current: String, correct: String): Int {

            var diff = toMin(correct) - toMin(current)
            var ans = 0
            for (step in intArrayOf(60, 15, 5, 1)) {
                ans += diff / step
                diff %= step
            }
            return ans

    }

}
