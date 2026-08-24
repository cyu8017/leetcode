// LeetCode 2194 - Cells in a Range on an Excel Sheet
// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution {
    fun cellsInRange(s: String): List<String> {
        val ans = mutableListOf<String>()
        var c = s[0]
        while (c <= s[3]) {
            var r = s[1]
            while (r <= s[4]) {
                ans.add("" + c + r)
                r++
            }
            c++
        }
        return ans
    }
}
