// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

class Solution {
    fun reversePrefix(s: String, k: Int): String {
        var arr = s.toCharArray()
        reverse(arr, 0, 0 + k)
        return String(arr)
    }

    private fun reverse(a: CharArray) { reverse(a, 0, a.size) }
    private fun reverse(a: CharArray, l: Int, r: Int) {
        var i = l
        var j = r - 1
        while (i < j) {
            var t = a[i]; a[i] = a[j]; a[j] = t
            i += 1; j -= 1
        }
    }
    private fun reverse(a: IntArray) { reverse(a, 0, a.size) }
    private fun reverse(a: IntArray, l: Int, r: Int) {
        var i = l
        var j = r - 1
        while (i < j) {
            var t = a[i]; a[i] = a[j]; a[j] = t
            i += 1; j -= 1
        }
    }
}
