// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

class Solution {
    fun simpleGraphExists(degrees: IntArray): Boolean {
        val n = degrees.size
        val d = degrees.clone()
        d.sort()
        var i = 0
        var j = n - 1
        while (i < j) {
            val tmp = d[i]
            d[i] = d[j]
            d[j] = tmp
            i++
            j--
        }
        var sum = 0L
        for (x in d) {
            if (x < 0 || x >= n) return false
            sum += x
        }
        if (sum % 2 == 1L) return false
        val prefix = LongArray(n + 1)
        for (idx in 0 until n) prefix[idx + 1] = prefix[idx] + d[idx]
        for (k in 1..n) {
            var right = 0L
            for (ii in k until n) right += if (d[ii] < k) d[ii].toLong() else k.toLong()
            if (prefix[k] > 1L * k * (k - 1) + right) return false
        }
        return true
    }
}
