// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution {

    fun percentageLetter(s: String, letter: Char): Int {

            var cnt = 0
            for (c in s.toCharArray()) if (c == letter) cnt++
            return cnt * 100 / s.length

    }

}
