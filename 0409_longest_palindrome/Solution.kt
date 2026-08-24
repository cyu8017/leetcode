// LeetCode 0409 - Longest Palindrome

// https://leetcode.com/problems/longest-palindrome/



class Solution {

    fun longestPalindrome(s: String): Int {

        val counts = IntArray(128)



        for (character in s) {

            counts[character.code]++

        }



        var length = 0

        var odd = false



        for (count in counts) {

            if (count == 0) {

                continue

            }



            length += count / 2 * 2



            if (count % 2 == 1) {

                odd = true

            }

        }



        return length + if (odd) 1 else 0

    }

}
