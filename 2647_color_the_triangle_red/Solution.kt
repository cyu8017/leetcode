
// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

class Solution {
    fun colorRed(n: Int): Array<IntArray> {
        val ans = ArrayList<IntArray>()
        for (i in 1..n) ans.add(intArrayOf(i, 1))
        var i = n % 2 + 2
        while (i <= n) {
            for (j in 2..(2 * (n - i) + 2)) ans.add(intArrayOf(i, j))
            i += 2
        }
        return ans.toTypedArray()
    }
}
