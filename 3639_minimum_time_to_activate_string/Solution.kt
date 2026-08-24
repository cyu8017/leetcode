// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

class Solution {
    private var n = 0
    private lateinit var order: IntArray
    private var total = 0L

    private fun countValid(t: Int): Long {
        val star = BooleanArray(n)
        for (i in 0..t) star[order[i]] = true
        var invalid = 0L
        var i = 0
        while (i < n) {
            if (star[i]) {
                i++
                continue
            }
            var j = i
            while (j < n && !star[j]) j++
            val L = (j - i).toLong()
            invalid += L * (L + 1) / 2
            i = j
        }
        return total - invalid
    }

    fun minTime(s: String, order: IntArray, k: Int): Int {
        this.order = order
        n = s.length
        total = 1L * n * (n + 1) / 2
        if (k > total) return -1
        var lo = 0
        var hi = n - 1
        var ans = -1
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            if (countValid(mid) >= k) {
                ans = mid
                hi = mid - 1
            } else lo = mid + 1
        }
        return ans
    }
}
