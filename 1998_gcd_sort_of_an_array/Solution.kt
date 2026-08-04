// LeetCode 1998
// https://leetcode.com/problems/gcd-sort-of-an-array/

class Solution {
    fun gcdSort(nums: IntArray): Boolean {
        val m = nums.maxOrNull()!!
        val parent = IntArray(m + 1) { it }
        fun find(x0: Int): Int {
            var x = x0
            while (parent[x] != x) {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        fun union(a: Int, b: Int) {
            val ra = find(a)
            val rb = find(b)
            if (ra != rb) parent[rb] = ra
        }
        val spf = IntArray(m + 1) { it }
        var i = 2
        while (i * i <= m) {
            if (spf[i] == i) {
                var j = i * i
                while (j <= m) {
                    if (spf[j] == j) spf[j] = i
                    j += i
                }
            }
            i++
        }
        for (x in nums.toHashSet()) {
            var y = x
            while (y > 1) {
                val p = spf[y]
                union(x, p)
                while (y % p == 0) y /= p
            }
        }
        val sorted = nums.sorted()
        for (idx in nums.indices) {
            if (find(nums[idx]) != find(sorted[idx])) return false
        }
        return true
    }
}
