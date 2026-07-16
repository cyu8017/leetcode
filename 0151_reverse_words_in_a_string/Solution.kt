class Solution {
    fun reverseWords(s: String): String = s.trim().split(Regex("\\s+")).filter { it.isNotEmpty() }.asReversed().joinToString(" ")
}