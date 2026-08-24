// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

class Solution {
    fun maxDifference(s: String, k: Int): Int {
        var n = s.length
        var ans = -1_000_000_000
        for (a in 0 until 5) {
            for (b in 0 until 5) {
                if (a == b) continue
                var prefA = IntArray(n + 1)
                var prefB = IntArray(n + 1)
                for (i in 0 until n) {
                    prefA[i + 1] = prefA[i]
                    prefB[i + 1] = prefB[i]
                    if (s[i] - '0' == a) prefA[i + 1]++
                    if (s[i] - '0' == b) prefB[i + 1]++
                }
                for (i in 0 until n) {
                    for (j in i + k - 1 until n) {
                        var fa = prefA[j + 1] - prefA[i]
                        var fb = prefB[j + 1] - prefB[i]
                        if (fa % 2 == 1 && fb % 2 == 0 && fb > 0) {
                            if (fa - fb > ans) ans = fa - fb
                        }
                    }
                }
            }
        }
        return ans
    }
}
