// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

class Solution {
    fun countGoodIntegers(n: Int, k: Int): Long {
        var half = (n + 1) / 2
        var start = 1
        for (i in 1 until half) { start *= 10 }
        var end = start * 10
        var seen = HashSet<String>()
        var ans = 0
        var fact = LongArray(n + 1)
        fact[0] = 1
        for (i in 1 ..n) { fact[i] = fact[i - 1] * i }
        for (h in start until end) {
            var s = Integer.toString(h)
            var pal = StringBuilder(s)
            var revStart = s.length - 1
            if (n % 2 == 1) revStart--
            run {
                var i = revStart
                while (i >= 0) {
                    pal.append(s[i])
                    i--
                }
            }
            if (pal.toString(.toLong()) % k != 0) continue
            var chars = pal.toString().toCharArray()
            chars.sort()
            var key = String(chars)
            if (!seen.add(key)) continue
            var cnt = IntArray(10)
            for (c in chars) { cnt[c - '0']++ }
            var total = fact[n]
            for (c in cnt) { total /= fact[c] }
            if (cnt[0] > 0) {
                var bad = fact[n - 1]
                cnt[0]--
                for (c in cnt) { bad /= fact[c] }
                cnt[0]++
                total -= bad
            }
            ans += total
        }
        return ans
    }
}
