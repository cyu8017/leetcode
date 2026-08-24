// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

class Solution {
    private fun modPow(a0: Long, e0: Long, mod: Int): Int {
        var a = a0 % mod
        var e = e0
        var r = 1L
        while (e > 0) {
            if ((e and 1L) != 0L) r = r * a % mod
            a = a * a % mod
            e = e shr 1
        }
        return r.toInt()
    }

    private fun key(a: Int, b: Int): Long {
        return (a  shl  32) or (b and 0xffffffffL)
    }

    fun countBalancedPermutations(num: String): Int {
        val mod = 1_000_000_007
        var cnt = IntArray(10)
        var sum = 0
        for (c in num.toCharArray()) {
            cnt[c - '0'] = cnt[c - '0'] + 1
            sum += c - '0'
        }
        if (sum % 2 == 1) return 0
        var n = num.length
        var halfN = n / 2
        var halfS = sum / 2
        var fact = IntArray(n + 1)
        var invF = IntArray(n + 1)
        fact[0] = 1
        for (i in 1 ..n) { fact[i] = (fact[i - 1] * i % mod) }
        invF[n] = modPow(fact[n], mod - 2, mod)
        run {
            var i = n
            while (i > 0) {
                invF[i - 1] = (invF[i] * i % mod)
                i--
            }
        }

        var dp = HashMap<Long, Int>()
        dp[key(0] = 0, 1)
        for (d in 0 ..9) {
            var ndp = HashMap<Long, Int>()
            for (kv in dp) {
                var st = kv.key
                var used = (st  shr  32)
                var s = st
                var ways = kv.value
                for (take in 0 ..cnt[d]) {
                    var nu = used + take
                    var ns = s + take * d
                    if (nu > halfN || ns > halfS) continue
                    var w = (ways * invF[take] % mod * invF[cnt[d] - take] % mod)
                    var nk = key(nu, ns)
                    ndp[nk] = (ndp.getOrDefault(nk, 0 + w) % mod)
                }
            }
            dp = ndp
        }
        var ans = dp.getOrDefault(key(halfN, halfS), 0)
        ans = (ans * fact[halfN] % mod * fact[n - halfN] % mod)
        for (d in 0 ..9) { ans = (ans * fact[cnt[d]] % mod) }
        return ans
    }
}
