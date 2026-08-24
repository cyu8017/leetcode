// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

class Solution {
    private var GOOD: MutableList<Int>? = null
    private var ready: Boolean = false

    private fun init() {
        if (ready) return
        val LIMIT = 1000000000L
        var cnt = HashMap<Int, Int>()
        var cubes = LongArray(1001)
        for (i in 0..1000) { cubes[i] = 1L * i * i * i }
        for (a in 1..1000) {
            for (b in a..1000) {
                var x = cubes[a] + cubes[b]
                if (x > LIMIT) break
                var xi = x
                cnt[xi] = cnt.getOrDefault(xi, 0 + 1)
            }
        }
        GOOD = ArrayList()
        for (kv in cnt) {
            if (kv.value > 1) GOOD.add(kv.key)
        }
        GOOD.sort()
        ready = true
    }

    fun findGoodIntegers(n: Int): IntArray {
        init()
        var lo = 0
        var hi = GOOD.size
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (GOOD[mid] <= n) lo = mid + 1
            else hi = mid
        }
        var ans = IntArray(lo)
        for (i in 0 until lo) { ans[i] = GOOD[i] }
        return ans
    }
}
