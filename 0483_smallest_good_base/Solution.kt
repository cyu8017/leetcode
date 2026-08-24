// LeetCode 0483 - Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/

import kotlin.math.log2

class Solution {
    fun smallestGoodBase(n: String): String {
        val num = n.toLong()
        for (length in log2(num.toDouble()).toInt() + 1 downTo 2) {
            var low = 2L
            var high = num - 1
            while (low <= high) {
                val mid = low + (high - low) / 2
                var total = 1L
                var power = 1L
                var ok = true
                repeat(length - 1) {
                    if (power > Long.MAX_VALUE / mid) {
                        ok = false
                        return@repeat
                    }
                    power *= mid
                    total += power
                    if (total > num) {
                        ok = false
                        return@repeat
                    }
                }
                when {
                    ok && total == num -> return mid.toString()
                    !ok || total > num -> high = mid - 1
                    else -> low = mid + 1
                }
            }
        }
        return (num - 1).toString()
    }
}
