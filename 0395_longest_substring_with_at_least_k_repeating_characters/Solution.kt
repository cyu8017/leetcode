// LeetCode 0395 - Longest Substring with At Least K Repeating Characters

// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/



class Solution {

    fun longestSubstring(s: String, k: Int): Int {

        if (s.isEmpty()) {

            return 0

        }



        val counts = s.groupingBy { it }.eachCount()

        for ((character, count) in counts) {

            if (count < k) {

                return s.split(character).maxOf { longestSubstring(it, k) }

            }

        }



        return s.length

    }

}
