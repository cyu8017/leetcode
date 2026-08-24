// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

import kotlin.math.sqrt

class Solution {
    fun isPrime(x: Long): Boolean {
        if (x < 2) return false
        val sqrtX = sqrt(x.toDouble()).toLong()
        for (i in 2..sqrtX) if (x % i == 0L) return false
        return true
    }

    fun sumOfLargestPrimes(s: String): Long {
        val st = HashSet<Long>()
        val n = s.length
        for (i in 0 until n) {
            var x = 0L
            for (j in i until n) {
                x = x * 10 + (s[j] - '0')
                if (isPrime(x)) st.add(x)
            }
        }
        val nums = ArrayList(st)
        nums.sort()
        var ans = 0L
        var i = nums.size - 1
        while (i >= 0 && nums.size - i <= 3) {
            ans += nums[i]
            i--
        }
        return ans
    }
}
