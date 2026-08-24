// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

class Solution {
    private fun sieve(n: Int): BooleanArray {
        var isP = BooleanArray(n)
        for (i in 2 until n) { isP[i] = true }
        var i = 2
        while (i * i < n) {
            if (isP[i]) {
                run {
                    var j = i * i
                    while (j < n) {
                        isP[j] = false
                        j += i
                    }
                }
            }
            i++
        }
        return isP
    }

    fun minOperations(n: Int, m: Int): Int {
        var isPrime = sieve(100000)
        if (isPrime[n]) return -1
        var dist = IntArray(100000)
        dist.fill(-1)
        var pq = PriorityQueue(compareBy { it[0] })
        pq.offer(intArrayOf(n, n))
        dist[n] = n
        while (!pq.isEmpty()) {
            var cur = pq.poll()
            var cost = cur[0]
            var `val` = cur[1]
            if (cost != dist[val]) continue
            if (val == m) return cost
            var s = val.toString().toCharArray()
            for (i in 0 until s.size) {
                var orig = s[i]
                for (d in intArrayOf(-1, 1)) {
                    var nd = (orig - '0') + d
                    if (nd < 0 || nd > 9) continue
                    if (i == 0 && nd == 0 && s.size > 1) continue
                    s[i] = (char) ('0' + nd)
                    var nv = String(s.toInt())
                    s[i] = orig
                    if (isPrime[nv]) continue
                    var nc = cost + nv
                    if (dist[nv] == -1 || nc < dist[nv]) {
                        dist[nv] = nc
                        pq.offer(intArrayOf(nc, nv))
                    }
                }
            }
        }
        return -1
    }
}
