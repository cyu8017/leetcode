// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

class Solution {
    fun groupStrings(strings: Array<String>): List<List<String>> {
        val groups = linkedMapOf<String, MutableList<String>>()

        for (text in strings) {
            val key = if (text.isEmpty()) {
                ""
            } else {
                val base = text[0].code
                text.map { ((it.code - base + 26) % 26).toString() }.joinToString(",")
            }
            groups.getOrPut(key) { mutableListOf() }.add(text)
        }

        return groups.values.toList()
    }
}
