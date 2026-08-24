// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

class Solution {

    private fun count(s: String, a: Char, b: Char): Long {

            var ca = 0; var ans = 0
            for (c in s.toCharArray()) {
                if (c == b) ans += ca
                if (c == a) ca++
            }
            return ans

    }


    fun maximumSubsequenceCount(text: String, pattern: String): Long {

            var a = pattern[0]; var b = pattern[1]
            return maxOf(count(a + text, a, b), count(text + b, a, b))

    }

}
