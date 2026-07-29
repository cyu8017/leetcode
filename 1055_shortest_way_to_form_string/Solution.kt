// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

class Solution {
    fun shortestWay(source: String, target: String): Int {
        val sourceSet = BooleanArray(26)
        for (ch in source) sourceSet[ch - 'a'] = true
        for (ch in target) {
            if (!sourceSet[ch - 'a']) return -1
        }
        var ans = 0
        var i = 0
        val n = target.length
        while (i < n) {
            ans++
            for (j in source.indices) {
                if (i < n && target[i] == source[j]) i++
            }
        }
        return ans
    }
}
