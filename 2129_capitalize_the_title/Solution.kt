// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

class Solution {
    fun capitalizeTitle(title: String): String {
        val parts = title.trim().split(" ").filter { it.isNotEmpty() }
        return parts.joinToString(" ") { w0 ->
            val w = w0.lowercase()
            if (w.length > 2) w[0].uppercaseChar() + w.substring(1) else w
        }
    }
}
