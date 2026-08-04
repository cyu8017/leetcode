// LeetCode 1390 - Four Divisors
// https://leetcode.com/problems/four-divisors/

class Solution {
    fun sumFourDivisors(nums: IntArray): Int {
        var ans = 0
        for (x in nums) {
            val ds = mutableSetOf<Int>()
            var d = 1
            while (d * d <= x) {
                if (x % d == 0) {
                    ds.add(d)
                    ds.add(x / d)
                }
                if (ds.size > 4) break
                d++
            }
            if (ds.size == 4) ans += ds.sum()
        }
        return ans
    }
}
