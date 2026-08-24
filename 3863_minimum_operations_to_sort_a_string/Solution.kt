// LeetCode 3863 - Minimum Operations To Sort A String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

class Solution {
    fun minOperations(s: String): Int {
        val n = s.length
        var sorted = true
        for (i in 1 until n) {
            if (s[i] < s[i - 1]) {
                sorted = false
                break
            }
        }
        if (sorted) return 0
        if (n == 2) return -1
        var mn = s[0]
        var mx = s[0]
        for (c in s) {
            if (c < mn) mn = c
            if (c > mx) mx = c
        }
        if (s[0] == mn || s[n - 1] == mx) return 1
        for (i in 1 until n - 1) {
            if (s[i] == mn || s[i] == mx) return 2
        }
        return 3
    }
}
