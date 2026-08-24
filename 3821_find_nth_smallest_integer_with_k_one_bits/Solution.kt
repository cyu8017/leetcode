// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find_nth_smallest_integer_with_k_one_bits/

class Solution {
    companion object {
        private const val MX = 50
        private val C: Array<LongArray> = Array(MX) { LongArray(MX + 1) }

        init {
            for (i in 0 until MX) {
                C[i][0] = 1
                for (j in 1..i) {
                    C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
                }
            }
        }
    }

    fun nthSmallest(n0: Long, k0: Int): Long {
        var n = n0
        var k = k0
        var ans = 0L
        for (i in 49 downTo 0) {
            if (n > C[i][k]) {
                n -= C[i][k]
                ans = ans or (1L shl i)
                k--
                if (k == 0) break
            }
        }
        return ans
    }
}
