// LeetCode 1409 - Queries on a Permutation With Key
// https://leetcode.com/problems/queries-on-a-permutation-with-key/

class Solution {
    fun processQueries(queries: IntArray, m: Int): IntArray {
        val values = ArrayList((1..m).toList())
        val answer = IntArray(queries.size)
        for (qi in queries.indices) {
            val query = queries[qi]
            val index = values.indexOf(query)
            answer[qi] = index
            values.removeAt(index)
            values.add(0, query)
        }
        return answer
    }
}
