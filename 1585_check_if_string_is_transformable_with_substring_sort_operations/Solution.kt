// LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
// https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

class Solution {
    fun isTransformable(s: String, t: String): Boolean {
        val positions = Array(10) { mutableListOf<Int>() }
        val heads = IntArray(10)
        for (i in s.indices) positions[s[i] - '0'].add(i)
        for (i in t.indices) {
            val d = t[i] - '0'
            if (heads[d] >= positions[d].size) return false
            val index = positions[d][heads[d]]
            for (smaller in 0 until d) {
                if (heads[smaller] < positions[smaller].size && positions[smaller][heads[smaller]] < index) {
                    return false
                }
            }
            heads[d]++
        }
        return true
    }
}
