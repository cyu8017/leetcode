// LeetCode 0344 - Reverse String

// https://leetcode.com/problems/reverse-string/



class Solution {

    fun reverseString(s: CharArray) {

        var left = 0

        var right = s.lastIndex



        while (left < right) {

            val temp = s[left]

            s[left] = s[right]

            s[right] = temp

            left++

            right--

        }

    }

}
