// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/


class Solution {
    fun findDuplicate(paths: Array<String>): List<List<String>> {
        val map = HashMap<String, MutableList<String>>()
        for (path in paths) {
            val parts = path.split(' ')
            val dir = parts[0]
            for (i in 1 until parts.size) {
                val left = parts[i].indexOf('(')
                val name = parts[i].substring(0, left)
                val content = parts[i].substring(left + 1, parts[i].length - 1)
                map.getOrPut(content) { ArrayList() }.add("$dir/$name")
            }
        }
        return map.values.filter { it.size > 1 }
    }
}
