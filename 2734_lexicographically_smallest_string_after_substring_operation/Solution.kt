// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

class Solution {
    fun smallestString(s: String): String {
        val arr = s.toCharArray()
        val n = arr.size
        var i = 0
        while (i < n && arr[i] == 'a') i++
        if (i == n) {
            arr[n - 1] = 'z'
            return String(arr)
        }
        while (i < n && arr[i] != 'a') {
            arr[i]--
            i++
        }
        return String(arr)
    }
}
