// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

class Solution {
    private val transitions = HashMap<String, MutableList<Char>>()
    private val memo = HashMap<String, Boolean>()

    fun pyramidTransition(bottom: String, allowed: List<String>): Boolean {
        transitions.clear()
        memo.clear()
        for (triple in allowed) {
            val key = triple.substring(0, 2)
            transitions.getOrPut(key) { ArrayList<Char>() }.add(triple[2])
        }
        return dfs(bottom)
    }

    private fun dfs(row: String): Boolean {
        if (row.length == 1) return true
        memo[row]?.let { return it }
        val options = ArrayList<List<Char>>()
        for (i in 0 until row.length - 1) {
            val key = row.substring(i, i + 2)
            if (!transitions.containsKey(key)) {
                memo[row] = false
                return false
            }
            options.add(transitions[key]!!)
        }
        val path = StringBuilder()
        val ok = build(0, options, path)
        memo[row] = ok
        return ok
    }

    private fun build(index: Int, options: List<List<Char>>, path: StringBuilder): Boolean {
        if (index == options.size) return dfs(path.toString())
        for (ch in options[index]) {
            path.append(ch)
            if (build(index + 1, options, path)) return true
            path.setLength(path.length - 1)
        }
        return false
    }
}
