// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

class Solution {
    private fun cost(x: Int, t: Int): Int {
        if (x == t) return 0
        if (x % t == 0 || t % x == 0) return 1
        return 2
    }

    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }

    fun minOperations(nums: IntArray): Int {
        val n = nums.size
        if (n <= 1) return 0
        var g = nums[0]
        var mn = nums[0]
        for (i in 1 until n) {
            g = gcd(g, nums[i])
            mn = minOf(mn, nums[i])
        }
        val cands = HashSet<Int>()
        for (x in nums) cands.add(x)
        var d = 1
        while (1L * d * d <= mn) {
            if (mn % d == 0) {
                cands.add(d)
                cands.add(mn / d)
            }
            d++
        }
        cands.add(g)
        var ans = Int.MAX_VALUE
        for (t in cands) {
            var sum = 0
            for (x in nums) {
                sum += cost(x, t)
                if (sum >= ans) break
            }
            ans = minOf(ans, sum)
        }
        return ans
    }
}
