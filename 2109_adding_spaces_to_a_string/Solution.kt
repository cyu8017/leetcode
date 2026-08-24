// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution {
    fun addSpaces(s: String, spaces: IntArray): String {
        StringBuilder b = StringBuilder(s.length + spaces.size)
        var j: Int = 0
        for (i in 0 until s.length) {
            if (j < spaces.size && spaces[j] == i) { b.append(' '); j++; }
            b.append(s[i])
        }
        return b.toString()
    }
}
