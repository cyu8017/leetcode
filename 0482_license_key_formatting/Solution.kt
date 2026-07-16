// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

class Solution {
    fun licenseKeyFormatting(s: String, k: Int): String {
        val chars = s.filter { it != '-' }.uppercase().toCharArray()
        if (chars.isEmpty()) {
            return ""
        }
        val firstLen = if (chars.size % k == 0) k else chars.size % k
        val parts = mutableListOf<String>()
        parts.add(String(chars, 0, firstLen))
        var index = firstLen
        while (index < chars.size) {
            parts.add(String(chars, index, k))
            index += k
        }
        return parts.joinToString("-")
    }
}
