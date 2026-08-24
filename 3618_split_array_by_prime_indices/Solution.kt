// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

class Solution {
    companion object {
        private const val M = 100010
        private var primesCache: BooleanArray? = null

        private fun primes(): BooleanArray {
            if (primesCache == null) {
                val p = BooleanArray(M) { true }
                p[0] = false
                p[1] = false
                for (i in 2 until M) {
                    if (p[i]) {
                        var j = i + i
                        while (j < M) {
                            p[j] = false
                            j += i
                        }
                    }
                }
                primesCache = p
            }
            return primesCache!!
        }
    }

    fun splitArray(nums: IntArray): Long {
        val pr = primes()
        var ans = 0L
        for (i in nums.indices) {
            if (pr[i]) ans += nums[i]
            else ans -= nums[i]
        }
        return kotlin.math.abs(ans)
    }
}
