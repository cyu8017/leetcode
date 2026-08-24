// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

class Solution {
    private val N: Int = 100001
    private val MOD: Int = 1000000007
    private var fact: LongArray? = null
    private var invFact: LongArray? = null
    private var ready: Boolean = false

    private fun qmi(a: Long, k: Long, p: Long): Long {
        var res = 1
        while (k != 0) {
            if ((k & 1) != 0) res = res * a % p
            k >>= 1
            a = a * a % p
        }
        return res
    }

    private fun init() {
        if (ready) return
        fact = LongArray(N)
        invFact = LongArray(N)
        fact[0] = invFact[0] = 1
        for (i in 1 until N) {
            fact[i] = fact[i - 1] * i % MOD
            invFact[i] = qmi(fact[i], MOD - 2, MOD)
        }
        ready = true
    }

    private fun comb(n: Int, k: Int): Long {
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD
    }

    fun countVisiblePeople(n: Int, pos: Int, k: Int): Int {
        init()
        var l = pos
        var r = n - pos - 1
        var ans = 0
        for (a in 0..minOf(k, l)) {
            var b = k - a
            if (b <= r) {
                ans = (ans + 2 * comb(l, a) % MOD * comb(r, b) % MOD) % MOD
            }
        }
        return ans
    }
}
