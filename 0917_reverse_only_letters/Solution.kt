// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

class Solution {
    fun reverseOnlyLetters(s: String): String {
        val arr = s.toCharArray()
        var i = 0
        var j = arr.size - 1
        while (i < j) {
            while (i < j && !arr[i].isLetter()) i++
            while (i < j && !arr[j].isLetter()) j--
            val tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i++
            j--
        }
        return String(arr)
    }
}
