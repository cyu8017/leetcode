// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

class Solution {
    fun countAsterisks(s: String): Int {
        var ans = 0
        var inside = false
        for (c in s) {
            if (c == '|') inside = !inside
            else if (c == '*' && !inside) ans++
        }
        return ans
    }
}
