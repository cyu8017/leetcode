// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

class Solution {
    fun substringXorQueries(s: String, queries: Array<IntArray>): Array<IntArray> {
        val pos = HashMap<Int, IntArray>()
        val n = s.length
        for (i in 0 until n) {
            if (s[i] == '0') {
                pos.putIfAbsent(0, intArrayOf(i, i))
                continue
            }
            var v = 0
            var j = i
            while (j < n && j < i + 30) {
                v = v * 2 + (s[j] - '0')
                pos.putIfAbsent(v, intArrayOf(i, j))
                j += 1
            }
        }
        val ans = Array(queries.size) { IntArray(2) }
        for (i in queries.indices) {
            val need = queries[i][0] xor queries[i][1]
            ans[i] = (pos[need] ?: intArrayOf(-1, -1)).copyOf()
        }
        return ans
    }
}
