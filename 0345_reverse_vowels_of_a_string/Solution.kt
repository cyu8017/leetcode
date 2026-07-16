// LeetCode 0345 - Reverse Vowels of a String

// https://leetcode.com/problems/reverse-vowels-of-a-string/



class Solution {

    fun reverseVowels(s: String): String {

        val chars = s.toCharArray()

        var left = 0

        var right = chars.lastIndex



        while (left < right) {

            while (left < right && !isVowel(chars[left])) {

                left++

            }

            while (left < right && !isVowel(chars[right])) {

                right--

            }

            val temp = chars[left]

            chars[left] = chars[right]

            chars[right] = temp

            left++

            right--

        }



        return String(chars)

    }



    private fun isVowel(ch: Char): Boolean {

        return ch in "aeiouAEIOU"

    }

}
