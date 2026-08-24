// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

class Solution {
    fun countPartitions(nums: IntArray, k: Int): Int {
        val mod = 1_000_000_007
        var sl = TreeMap<Int, Int>()
        var n = nums.size
        var f = IntArray(n + 1)
        var g = IntArray(n + 1)
        f[0] = g[0] = 1
        var l = 1
        var r = 1
        while (r <= n) {
            sl.merge(nums[r - 1], 1, Integer::sum)
            while (sl.lastKey() - sl.firstKey() > k) {
                var v = nums[l - 1]
                var c = sl[v]
                if (c == 1) sl.remove(v)
                else sl[v] = c - 1
                l = l + 1
            }
            f[r] = g[r - 1]
            if (l >= 2) f[r] = (f[r] - g[l - 2] + mod) % mod
            g[r] = (g[r - 1] + f[r]) % mod
            r = r + 1
        }
        return f[n]
    }
}
