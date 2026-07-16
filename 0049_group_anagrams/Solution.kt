// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val groups = HashMap<String, MutableList<String>>()

        for (word in strs) {
            val key = word.toCharArray().sorted().joinToString("")
            groups.getOrPut(key) { mutableListOf() }.add(word)
        }

        val result = groups.values.map { it.sorted() }.toMutableList()
        result.sortByDescending { minGroupIndex(strs, it) }
        return result
    }

    private fun minGroupIndex(strs: Array<String>, group: List<String>): Int {
        var min = strs.size
        for (word in group) {
            for (i in strs.indices) {
                if (strs[i] == word) {
                    min = minOf(min, i)
                    break
                }
            }
        }
        return min
    }
}
