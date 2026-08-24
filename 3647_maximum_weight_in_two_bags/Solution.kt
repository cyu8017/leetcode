// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

class Solution {
    fun maxWeight(weights: IntArray, w1: Int, w2: Int): Int {
        var f = Array(w1 + 1) { IntArray(w2 + 1) }
        for (x in weights) {
            for (j in w1 downTo 0) {
                for (k in w2 downTo 0) {
                    if (x <= j) f[j][k] = maxOf(f[j][k], f[j - x][k] + x)
                    if (x <= k) f[j][k] = maxOf(f[j][k], f[j][k - x] + x)
                }
            }
        }
        return f[w1][w2]
    }
}
