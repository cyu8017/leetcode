// LeetCode 3823 - Reverse Letters Then Special Characters in a String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

class Solution {
    fun reverseByType(s: String): String {
        val a = ArrayList<Char>()
        val b = ArrayList<Char>()
        for (c in s.toCharArray()) {
            if ((c in 'A'..'Z') || (c in 'a'..'z')) a.add(c)
            else b.add(c)
        }
        var j = a.size
        var k = b.size
        val arr = s.toCharArray()
        for (i in arr.indices) {
            if ((arr[i] in 'A'..'Z') || (arr[i] in 'a'..'z')) arr[i] = a[--j]
            else arr[i] = b[--k]
        }
        return String(arr)
    }
}
