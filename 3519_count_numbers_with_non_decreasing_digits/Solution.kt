// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

class Solution {
    companion object {
        const val MOD = 1_000_000_007
    }

    fun toDigits(s0: String, b: Int): MutableList<Int> {
        var s = s0
        if (s == "0") return mutableListOf(0)
        val digs = ArrayList<Int>()
        while (!(s.length == 1 && s[0] == '0')) {
            var rem = 0
            val q = StringBuilder()
            for (c in s) {
                val cur = rem * 10 + (c - '0')
                val d = cur / b
                rem = cur % b
                if (q.isNotEmpty() || d != 0) q.append(('0'.code + d).toChar())
            }
            digs.add(rem)
            s = if (q.isEmpty()) "0" else q.toString()
        }
        digs.reverse()
        return digs
    }

    fun dec(s: String): String {
        val a = s.toCharArray()
        var i = a.size - 1
        while (i >= 0 && a[i] == '0') {
            a[i] = '9'
            i--
        }
        if (i < 0) return "0"
        a[i] = (a[i].code - 1).toChar()
        val t = String(a)
        var p = 0
        while (p + 1 < t.length && t[p] == '0') p++
        return t.substring(p)
    }

    fun countUpto(digs: List<Int>, b: Int): Int {
        val m = digs.size
        val memo = HashMap<String, Int>()
        return dfs(0, 0, true, digs, b, m, memo)
    }

    fun dfs(pos: Int, last: Int, tight: Boolean, digs: List<Int>, b: Int, m: Int, memo: HashMap<String, Int>): Int {
        if (pos == m) return 1
        val key = "$pos,$last,${if (tight) 1 else 0}"
        memo[key]?.let { return it }
        val up = if (tight) digs[pos] else b - 1
        var res = 0
        for (d in last..up) {
            res = (res + dfs(pos + 1, d, tight && d == up, digs, b, m, memo)) % MOD
        }
        memo[key] = res
        return res
    }

    fun countNumbers(l: String, r: String, b: Int): Int {
        val rd = toDigits(r, b)
        val ld = toDigits(dec(l), b)
        return (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD
    }
}
