// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/

class Solution {
    fun smallestUniqueSubarray(nums: IntArray): Int {
        val n = nums.size
        val sa = Array(n) { it }
        var rank = nums.copyOf()
        var width = 1
        while (width < n) {
            val w = width
            val r = rank
            sa.sortWith(Comparator { a, b ->
                if (r[a] != r[b]) r[a].compareTo(r[b])
                else {
                    val ra = if (a + w < n) r[a + w] else -1
                    val rb = if (b + w < n) r[b + w] else -1
                    ra.compareTo(rb)
                }
            })
            val next = IntArray(n)
            for (i in 1 until n) {
                val a = sa[i - 1]
                val b = sa[i]
                val different = rank[a] != rank[b]
                val ra = if (a + width < n) rank[a + width] else -1
                val rb = if (b + width < n) rank[b + width] else -1
                next[b] = if (different || ra != rb) next[a] + 1 else next[a]
            }
            rank = next
            if (rank[sa[n - 1]] == n - 1) break
            width = width shl 1
        }
        val pos = IntArray(n)
        for (i in 0 until n) pos[sa[i]] = i
        val lcp = IntArray(maxOf(0, n - 1))
        var height = 0
        for (i in 0 until n) {
            val p = pos[i]
            if (p == n - 1) {
                height = 0
                continue
            }
            val j = sa[p + 1]
            while (i + height < n && j + height < n && nums[i + height] == nums[j + height]) height++
            lcp[p] = height
            if (height > 0) height--
        }
        var ans = n
        for (p in 0 until n) {
            val start = sa[p]
            var need = 1
            if (p > 0 && lcp[p - 1] + 1 > need) need = lcp[p - 1] + 1
            if (p + 1 < n && lcp[p] + 1 > need) need = lcp[p] + 1
            if (need <= n - start && need < ans) ans = need
        }
        return ans
    }
}
