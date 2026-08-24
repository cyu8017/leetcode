// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution {
    fun getSmallestString(s: String): String {
        var arr = s.toCharArray()
        var n = arr.size
        for (i in 1 until n) {
            var a = arr[i - 1]
            var b = arr[i]
            if (a > b && (a % 2) == (b % 2)) {
                arr[i - 1] = b; arr[i] = a
                return String(arr)
            }
        }
        return s
    }
}
