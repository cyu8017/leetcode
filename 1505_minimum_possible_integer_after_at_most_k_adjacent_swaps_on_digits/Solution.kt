// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

import java.util.ArrayDeque

class Solution {
    fun minInteger(num: String, k: Int): String {
        var rem = k
        val positions = Array(10) { ArrayDeque<Int>() }
        for (i in num.indices) {
            positions[num[i] - '0'].addLast(i)
        }
        val fw = FenwickTree(num.length)
        val out = StringBuilder()
        for (i in num.indices) {
            for (digit in 0..9) {
                if (positions[digit].isEmpty()) continue
                val index = positions[digit].peekFirst()
                val cost = index - fw.sum(index)
                if (cost <= rem) {
                    rem -= cost
                    positions[digit].pollFirst()
                    fw.add(index, 1)
                    out.append(('0'.code + digit).toChar())
                    break
                }
            }
        }
        return out.toString()
    }

    private class FenwickTree(n: Int) {
        private val bit = IntArray(n + 1)

        fun add(i: Int, delta: Int) {
            var idx = i + 1
            while (idx < bit.size) {
                bit[idx] += delta
                idx += idx and -idx
            }
        }

        fun sum(i: Int): Int {
            var idx = i
            var out = 0
            while (idx > 0) {
                out += bit[idx]
                idx -= idx and -idx
            }
            return out
        }
    }
}
