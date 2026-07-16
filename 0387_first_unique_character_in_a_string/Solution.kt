// LeetCode 0387 - First Unique Character in a String

// https://leetcode.com/problems/first-unique-character-in-a-string/



class Solution {

    fun firstUniqChar(s: String): Int {

        val counts = mutableMapOf<Char, Int>()

        for (ch in s) {

            counts[ch] = counts.getOrDefault(ch, 0) + 1

        }



        for ((index, ch) in s.withIndex()) {

            if (counts.getValue(ch) == 1) {

                return index

            }

        }

        return -1

    }

}
