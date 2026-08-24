// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

class Solution {
    private fun isPrime(n: Int): Boolean {
        if (n < 2) return false
        var i = 2
        while (i <= n / i) {
            if (n % i == 0) return false
            i++
        }
        return true
    }

    fun maximumPrimeDifference(nums: IntArray): Int {
        var i = 0
        while (true) {
            if (isPrime(nums[i])) {
                var j = nums.size - 1
                while (true) {
                    if (isPrime(nums[j])) return j - i
                    j--
                }
            }
            i++
        }
    }
}
