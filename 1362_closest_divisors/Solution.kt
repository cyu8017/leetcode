// LeetCode 1362 - Closest Divisors
// https://leetcode.com/problems/closest-divisors/

class Solution {
    fun closestDivisors(num: Int): IntArray {
        var best: IntArray? = null
        for (x in intArrayOf(num + 1, num + 2)) {
            var a = kotlin.math.sqrt(x.toDouble()).toInt()
            while (a > 0) {
                if (x % a == 0) {
                    val pair = intArrayOf(a, x / a)
                    if (best == null || pair[1] - pair[0] < best[1] - best[0]) {
                        best = pair
                    }
                    break
                }
                a--
            }
        }
        return best!!
    }
}
