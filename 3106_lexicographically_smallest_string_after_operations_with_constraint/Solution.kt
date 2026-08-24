// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

class Solution {
    fun getSmallestString(s: String, k: Int): String {
        var arr = s.toCharArray()
        for (i in 0 until arr.size) {
            var c1 = arr[i]
            for (char c2 = 'a'; c2 < c1; c2++) {
                var d = minOf(c1 - c2, 26 - (c1 - c2))
                if (d <= k) {
                    arr[i] = c2
                    k -= d
                    break
                }
            }
        }
        return String(arr)
    }
}
