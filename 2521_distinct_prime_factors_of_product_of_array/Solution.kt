// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution {
    fun distinctPrimeFactors(nums: IntArray): Int {
        var set = HashSet<Int>()
        for (num in nums) {
            var x = num
            var p = 2
            while (p * p <= x) {
                if (x % p == 0) {
                    set.add(p)
                    while (x % p == 0) x /= p
                }
                p = p + 1
            }
            if (x > 1) set.add(x)
        }
        return set.size
    }
}
