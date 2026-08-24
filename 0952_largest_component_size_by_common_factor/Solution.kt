// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

class Solution {
    private lateinit var parent: IntArray

    fun largestComponentSize(nums: IntArray): Int {
        var mx = 0
        for (x in nums) mx = maxOf(mx, x)
        parent = IntArray(mx + 1) { it }
        for (num in nums) {
            for (f in factors(num)) unite(num, f)
        }
        val cnt = HashMap<Int, Int>()
        var ans = 0
        for (num in nums) {
            val r = find(num)
            val c = cnt.getOrDefault(r, 0) + 1
            cnt[r] = c
            ans = maxOf(ans, c)
        }
        return ans
    }

    private fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    private fun unite(a: Int, b: Int) {
        parent[find(a)] = find(b)
    }

    private fun factors(x: Int): List<Int> {
        var x = x
        val res = mutableListOf<Int>()
        var d = 2
        while (d.toLong() * d <= x) {
            if (x % d == 0) {
                res.add(d)
                while (x % d == 0) x /= d
            }
            d++
        }
        if (x > 1) res.add(x)
        return res
    }
}
