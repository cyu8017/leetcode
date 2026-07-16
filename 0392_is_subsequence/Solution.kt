// LeetCode 0392 - Is Subsequence

// https://leetcode.com/problems/is-subsequence/



class Solution {

    fun isSubsequence(s: String, t: String): Boolean {

        var index = 0



        for (char in t) {

            if (index < s.length && s[index] == char) {

                index++

            }

        }



        return index == s.length

    }

}
