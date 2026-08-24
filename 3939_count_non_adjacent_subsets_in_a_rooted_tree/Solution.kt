// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

class Solution {
    fun countNonAdjacentSubsets(parent: IntArray, nums: IntArray, k: Int): Int {
        val mod = 1000000007L
        val n = parent.size
        val children = Array(n) { ArrayList<Int>() }
        for (i in 1 until n) children[parent[i]].add(i)
        val dp0 = arrayOfNulls<LongArray>(n)
        val dp1 = arrayOfNulls<LongArray>(n)
        for (u in n - 1 downTo 0) {
            var a = LongArray(k)
            var b = LongArray(k)
            a[0] = 1
            b[((nums[u] % k) + k) % k] = 1
            for (v in children[u]) {
                val na = LongArray(k)
                val nb = LongArray(k)
                for (x in 0 until k) {
                    for (y in 0 until k) {
                        val allChild = (dp0[v]!![y] + dp1[v]!![y]) % mod
                        na[(x + y) % k] = (na[(x + y) % k] + a[x] * allChild) % mod
                        nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v]!![y]) % mod
                    }
                }
                a = na
                b = nb
            }
            dp0[u] = a
            dp1[u] = b
        }
        var ans = (dp0[0]!![0] + dp1[0]!![0] - 1) % mod
        if (ans < 0) ans += mod
        return ans.toInt()
    }
}
