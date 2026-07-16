// LeetCode 0383 - Ransom Note

// https://leetcode.com/problems/ransom-note/



class Solution {

    fun canConstruct(ransomNote: String, magazine: String): Boolean {

        val counts = mutableMapOf<Char, Int>()

        for (ch in magazine) {

            counts[ch] = counts.getOrDefault(ch, 0) + 1

        }



        for (ch in ransomNote) {

            val remaining = counts.getOrDefault(ch, 0)

            if (remaining == 0) {

                return false

            }

            counts[ch] = remaining - 1

        }

        return true

    }

}
