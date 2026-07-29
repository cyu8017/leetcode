// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

class Solution {
    fun expand(s: String): Array<String> {
        val groups = mutableListOf<List<String>>()
        var i = 0
        while (i < s.length) {
            if (s[i] == '{') {
                var j = i + 1
                while (s[j] != '}') j++
                val parts = s.substring(i + 1, j).split(",").sorted()
                groups.add(parts)
                i = j + 1
            } else {
                groups.add(listOf(s[i].toString()))
                i++
            }
        }
        var ans = listOf("")
        for (group in groups) {
            val next = mutableListOf<String>()
            for (prefix in ans) {
                for (ch in group) next.add(prefix + ch)
            }
            ans = next
        }
        return ans.toTypedArray()
    }
}
