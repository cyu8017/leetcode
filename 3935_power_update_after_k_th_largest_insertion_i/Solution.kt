// LeetCode 3935 - Power Update After K Th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

class Solution {
    private fun merge(st: java.util.TreeMap<Int, Int>, x: Int, v: Int) {
        val c = st.getOrDefault(x, 0)
        if (c + v == 0) st.remove(x) else st[x] = c + v
    }

    fun powerUpdate(nums: IntArray, p0: Int, queries: Array<IntArray>): IntArray {
        val L = java.util.TreeMap<Int, Int>()
        val R = java.util.TreeMap<Int, Int>()
        var sz1 = 0
        var sz2 = nums.size
        for (x in nums) merge(R, x, 1)
        val mod = 1000000007
        val ans = IntArray(queries.size)
        var p = p0
        for (qi in queries.indices) {
            val value = queries[qi][0]
            val k = queries[qi][1]
            merge(R, value, 1)
            sz2++
            var node = R.firstKey()
            merge(R, node, -1)
            sz2--
            merge(L, node, 1)
            sz1++
            while (sz2 < k) {
                node = L.lastKey()
                merge(L, node, -1)
                sz1--
                merge(R, node, 1)
                sz2++
            }
            while (sz2 > k) {
                node = R.firstKey()
                merge(R, node, -1)
                sz2--
                merge(L, node, 1)
                sz1++
            }
            val x = R.firstKey()
            p = qpow(p.toLong(), x, mod)
            ans[qi] = p
        }
        return ans
    }

    private fun qpow(a0: Long, b0: Int, mod: Int): Int {
        var a = a0
        var b = b0
        var ans = 1L
        while (b > 0) {
            if ((b and 1) != 0) ans = ans * a % mod
            a = a * a % mod
            b = b shr 1
        }
        return ans.toInt()
    }
}
