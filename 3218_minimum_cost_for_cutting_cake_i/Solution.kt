// LeetCode 3218 - Minimum Cost for Cutting Cake I
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

class Solution {
    fun minimumCost(m: Int, n: Int, horizontalCut: IntArray, verticalCut: IntArray): Int {
        horizontalCut.sort()
        reverse(horizontalCut)
        verticalCut.sort()
        reverse(verticalCut)
        var i = 0
        var j = 0
        var h = 1
        var v = 1
        var ans = 0
        while (i < m - 1 || j < n - 1) {
            if (j == n - 1 || (i < m - 1 && horizontalCut[i] > verticalCut[j])) {
                ans += horizontalCut[i] * v
                h++
                i++
            } else {
                ans += verticalCut[j] * h
                v++
                j++
            }
        }
        return ans
    }

    private fun reverse(a: IntArray) {
        var l = 0
        var r = a.size - 1
        while (l < r) {
            val t = a[l]
            a[l] = a[r]
            a[r] = t
            l++
            r--
        }
    }
}
