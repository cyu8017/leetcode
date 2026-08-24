// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

class Solution {
    fun minReverseOperations(n: Int, p: Int, banned: IntArray, k: Int): IntArray {
        val ban = HashSet<Int>()
        for (b in banned) ban.add(b)
        val ans = IntArray(n) { -1 }
        ans[p] = 0
        val q = ArrayDeque<IntArray>()
        q.add(intArrayOf(p, 0))
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            val i = cur[0]
            val d = cur[1]
            var lo = i - (k - 1)
            if (lo < 0) lo = 0
            var hi = i
            if (hi > n - k) hi = n - k
            for (L in lo..hi) {
                val R = L + k - 1
                val ni = L + R - i
                if (ni < 0 || ni >= n || ni in ban || ans[ni] != -1) continue
                ans[ni] = d + 1
                q.add(intArrayOf(ni, d + 1))
            }
        }
        return ans
    }
}
