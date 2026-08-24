// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution {

    fun numberOfWays(s: String): Long {

            var total0 = 0; var total1 = 0
            for (c in s.toCharArray()) {
                if (c == '0') total0++
                else total1++
            }
            var left0 = 0; var left1 = 0
            var ans = 0
            for (c in s.toCharArray()) {
                if (c == '0') {
                    ans += left1 * (total1 - left1)
                    left0++
                } else {
                    ans += left0 * (total0 - left0)
                    left1++
                }
            }
            return ans

    }

}
