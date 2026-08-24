// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

import java.util.TreeSet

class Solution {
    fun minOperations(s: String, k: Int): Int {
        val n = s.length
        val ts = Array(2) { TreeSet<Int>() }
        for (i in 0..n) ts[i % 2].add(i)
        var cnt0 = 0
        for (c in s) if (c == '0') cnt0++
        ts[cnt0 % 2].remove(cnt0)
        var q = ArrayList<Int>()
        q.add(cnt0)
        var ans = 0
        while (q.isNotEmpty()) {
            val nq = ArrayList<Int>()
            for (cur in q) {
                if (cur == 0) return ans
                val l = cur + k - 2 * minOf(cur, k)
                val r = cur + k - 2 * maxOf(k - n + cur, 0)
                val t = ts[l % 2]
                var it = t.ceiling(l)
                while (it != null && it <= r) {
                    nq.add(it)
                    t.remove(it)
                    it = t.ceiling(l)
                }
            }
            q = nq
            ans++
        }
        return -1
    }
}
