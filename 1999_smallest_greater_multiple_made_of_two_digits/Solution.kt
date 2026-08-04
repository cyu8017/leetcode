// LeetCode 1999
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

class Solution {
    fun findInteger(k: Int, digit1: Int, digit2: Int): Int {
        val digits = sortedSetOf(digit1, digit2)
        val q = ArrayDeque<Long>()
        val seen = HashSet<Long>()
        for (d in digits) {
            if (d != 0) {
                q.add(d.toLong())
                seen.add(d.toLong())
            }
        }
        if (q.isEmpty()) return -1
        val limit = Int.MAX_VALUE.toLong()
        while (q.isNotEmpty()) {
            val x = q.removeFirst()
            if (x > k && x % k == 0L) return x.toInt()
            for (d in digits) {
                val nx = x * 10 + d
                if (nx <= limit && nx !in seen) {
                    seen.add(nx)
                    q.add(nx)
                }
            }
        }
        return -1
    }
}
