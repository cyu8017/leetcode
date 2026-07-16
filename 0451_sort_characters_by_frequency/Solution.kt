// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

class Solution {
    fun frequencySort(s: String): String {
        val counts = HashMap<Char, Int>()
        for (ch in s) {
            counts[ch] = counts.getOrDefault(ch, 0) + 1
        }
        val ordered = counts.entries.sortedWith(
            compareByDescending<Map.Entry<Char, Int>> { it.value }.thenBy { it.key },
        )
        return buildString {
            for ((ch, count) in ordered) {
                repeat(count) { append(ch) }
            }
        }
    }
}
