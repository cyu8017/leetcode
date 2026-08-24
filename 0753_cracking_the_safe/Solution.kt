// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

class Solution {
    private val seen = HashSet<String>()
    private val path = ArrayList<Char>()

    fun crackSafe(n: Int, k: Int): String {
        seen.clear()
        path.clear()
        val start = "0".repeat(n - 1)
        dfs(start, k)
        val result = StringBuilder()
        for (ch in path) result.append(ch)
        return result.toString() + start
    }

    private fun dfs(node: String, k: Int) {
        for (d in 0 until k) {
            val digit = ('0'.code + d).toChar()
            val edge = node + digit
            if (seen.add(edge)) {
                dfs(edge.substring(1), k)
                path.add(digit)
            }
        }
    }
}
