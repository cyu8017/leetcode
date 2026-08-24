// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

class Solution {
    fun putMarbles(weights: IntArray, k: Int): Long {
        var n = weights.size
        if (k == 1 || k == n) return 0
        var pair = IntArray(n - 1)
        for (i in 0 until n - 1) { pair[i] = weights[i] + weights[i + 1] }
        pair.sort()
        var mn = 0
        var mx = 0
        for (i in 0 until k - 1) {
            mn += pair[i]
            mx += pair[n - 2 - i]
        }
        return mx - mn
    }
}
