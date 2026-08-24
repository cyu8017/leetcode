// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

class Solution {
    fun minOperations(initial: String, target: String): Int {
        var m = initial.length, n = target.length
        var f = IntArray(m + 1)[]
        for (i in 0 until = m) { f[i] = IntArray(n + 1) }
        var mx = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (initial[i] == target[j]) {
                    f[i + 1][j + 1] = f[i][j] + 1
                    mx = maxOf(mx, f[i + 1][j + 1])
                }
            }
        }
        return m + n - 2 * mx
    }
}
