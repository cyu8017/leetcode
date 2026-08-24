// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

class Solution {
    fun canConvert(str1: String, str2: String): Boolean {
        if (str1 == str2) return true
        val mapping = mutableMapOf<Char, Char>()
        for (i in str1.indices) {
            val a = str1[i]
            val b = str2[i]
            if (a in mapping && mapping[a] != b) return false
            mapping[a] = b
        }
        return str2.toSet().size < 26
    }
}
