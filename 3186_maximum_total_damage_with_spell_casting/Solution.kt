// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

class Solution {
    private var power: IntArray? = null
    private var nxt: IntArray? = null
    private var f: LongArray? = null
    private var cnt: MutableMap<Int, Int>? = null
    private var n: Int = 0

    fun maximumTotalDamage(power: IntArray): Long {
        n = power.size
        power.sort()
        this.power = power
        cnt = HashMap()
        nxt = IntArray(n)
        f = LongArray(n)
        for (i in 0 until n) {
            cnt.merge(power[i], 1, Integer::sum)
            nxt[i] = lowerBound(power, power[i] + 3)
        }
        return dfs(0)
    }

    private fun dfs(i: Int): Long {
        if (i >= n) {
            return 0
        }
        if (f[i] != 0) {
            return f[i]
        }
        var a = dfs(i + cnt[power[i]])
        var b = power[i] * cnt[power[i]] + dfs(nxt[i])
        return f[i] = maxOf(a, b)
    }

    private fun lowerBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (a[mid] < x) {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        return lo
    }
}
