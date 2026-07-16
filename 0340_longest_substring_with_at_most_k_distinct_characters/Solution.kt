// LeetCode 0340 - Longest Substring with At Most K Distinct Characters

// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/



class Solution {

    fun lengthOfLongestSubstringKDistinct(s: String, k: Int): Int {

        if (k == 0) {

            return 0

        }



        val counts = mutableMapOf<Char, Int>()

        var left = 0

        var best = 0



        for (right in s.indices) {

            val ch = s[right]

            counts[ch] = counts.getOrDefault(ch, 0) + 1



            while (counts.size > k) {

                val leftChar = s[left]

                val nextCount = counts.getValue(leftChar) - 1

                if (nextCount == 0) {

                    counts.remove(leftChar)

                } else {

                    counts[leftChar] = nextCount

                }

                left++

            }



            best = maxOf(best, right - left + 1)

        }



        return best

    }

}
