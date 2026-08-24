// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

class Solution {
    fun checkDistances(s: String, distance: IntArray): Boolean {
        val first = IntArray(26) { -1 }
        for (i in s.indices) {
            val c = s[i] - 'a'
            if (first[c] == -1) first[c] = i
            else if (i - first[c] - 1 != distance[c]) return false
        }
        return true
    }
}
