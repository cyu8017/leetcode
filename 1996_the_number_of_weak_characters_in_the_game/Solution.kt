// LeetCode 1996
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

class Solution {
    fun numberOfWeakCharacters(properties: Array<IntArray>): Int {
        properties.sortWith(compareBy<IntArray> { it[0] }.thenByDescending { it[1] })
        var ans = 0
        var maxDef = 0
        for (i in properties.indices.reversed()) {
            if (properties[i][1] < maxDef) ans++ else maxDef = properties[i][1]
        }
        return ans
    }
}
