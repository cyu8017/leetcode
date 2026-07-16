class Solution {
    fun lengthOfLongestSubstringTwoDistinct(s: String): Int {
        val counts = mutableMapOf<Char, Int>(); var left = 0; var best = 0
        for (right in s.indices) {
            counts[s[right]] = (counts[s[right]] ?: 0) + 1
            while (counts.size > 2) {
                val c = s[left++]
                if (counts[c] == 1) counts.remove(c) else counts[c] = counts[c]!! - 1
            }
            best = maxOf(best, right - left + 1)
        }
        return best
    }
}