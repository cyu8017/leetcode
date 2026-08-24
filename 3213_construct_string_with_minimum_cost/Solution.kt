// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

class Solution {
    private class Hashing(word: String, bas: Long, private val mod: Long) {
        val p: LongArray
        val h: LongArray

        init {
            val n = word.length
            p = LongArray(n + 1)
            h = LongArray(n + 1)
            p[0] = 1
            for (i in 1..n) {
                p[i] = p[i - 1] * bas % mod
                h[i] = (h[i - 1] * bas + word[i - 1].code) % mod
            }
        }

        fun query(l: Int, r: Int): Long {
            return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod
        }
    }

    fun minimumCost(target: String, words: Array<String>, costs: IntArray): Int {
        val bas = 13331L
        val mod = 998244353L
        val inf = Int.MAX_VALUE / 2
        val n = target.length
        val hashing = Hashing(target, bas, mod)
        val f = IntArray(n + 1) { inf }
        f[0] = 0
        val ss = HashSet<Int>()
        for (w in words) ss.add(w.length)
        val lengths = ArrayList(ss)
        lengths.sort()
        val d = HashMap<Long, Int>()
        for (i in words.indices) {
            var x = 0L
            for (c in words[i]) x = (x * bas + c.code) % mod
            if (!d.containsKey(x) || costs[i] < d[x]!!) d[x] = costs[i]
        }
        for (i in 1..n) {
            for (j in lengths) {
                if (j > i) break
                val x = hashing.query(i - j + 1, i)
                if (d.containsKey(x)) f[i] = minOf(f[i], f[i - j] + d[x]!!)
            }
        }
        return if (f[n] >= inf) -1 else f[n]
    }
}
