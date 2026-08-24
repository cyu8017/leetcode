// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

class Solution {
    fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }

    fun maxGCDScore(nums: IntArray, k: Int): Long {
        val n = nums.size
        val cnt = IntArray(n)
        for (i in 0 until n) {
            var x = nums[i]
            while (x % 2 == 0) {
                cnt[i]++
                x /= 2
            }
        }
        var ans = 0L
        for (l in 0 until n) {
            var g = 0
            var mi = Int.MAX_VALUE
            var t = 0
            for (r in l until n) {
                g = gcd(g, nums[r])
                if (cnt[r] < mi) {
                    mi = cnt[r]
                    t = 1
                } else if (cnt[r] == mi) t++
                var score = 1L * g * (r - l + 1)
                if (t <= k) score *= 2
                ans = maxOf(ans, score)
            }
        }
        return ans
    }
}
