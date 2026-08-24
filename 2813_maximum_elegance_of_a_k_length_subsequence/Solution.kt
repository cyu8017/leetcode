// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

class Solution {
    fun findMaximumElegance(items: Array<IntArray>, k: Int): Long {
        items.sortWith(compareByDescending { it[0] })
        val seen = HashSet<Int>()
        var total = 0L
        val dup = ArrayList<Int>()
        for (i in 0 until k) {
            total += items[i][0]
            val c = items[i][1]
            if (seen.contains(c)) dup.add(items[i][0]) else seen.add(c)
        }
        var ans = total + 1L * seen.size * seen.size
        for (i in k until items.size) {
            val c = items[i][1]
            if (seen.contains(c) || dup.isEmpty()) continue
            total += items[i][0] - dup[dup.size - 1]
            dup.removeAt(dup.size - 1)
            seen.add(c)
            ans = maxOf(ans, total + 1L * seen.size * seen.size)
        }
        return ans
    }
}
