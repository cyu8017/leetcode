// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

class Fancy {
    private val MOD = 1_000_000_007L
    private val vals = mutableListOf<Long>()
    private var mul = 1L
    private var add = 0L

    fun append(`val`: Int) {
        val v = ((`val`.toLong() - add) % MOD + MOD) % MOD
        vals.add(v * modInverse(mul) % MOD)
    }

    fun addAll(inc: Int) {
        add = (add + inc) % MOD
    }

    fun multAll(m: Int) {
        mul = mul * m % MOD
        add = add * m % MOD
    }

    fun getIndex(idx: Int): Int {
        if (idx >= vals.size) return -1
        return ((vals[idx] * mul + add) % MOD).toInt()
    }

    private fun modInverse(a: Long): Long {
        var x = a % MOD
        var y = MOD - 2
        var res = 1L
        while (y > 0) {
            if (y and 1L == 1L) res = res * x % MOD
            x = x * x % MOD
            y = y shr 1
        }
        return res
    }
}
