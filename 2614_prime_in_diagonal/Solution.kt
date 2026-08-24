// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

class Solution {
    fun diagonalPrime(nums: Array<IntArray>): Int {
        var n = nums.size
        var best = 0
        for (i in 0 until n) {
            var a = nums[i][i]
            var b = nums[i][n - 1 - i]
            if (isPrime(a) && a > best) best = a
            if (isPrime(b) && b > best) best = b
        }
        return best
    }

    private fun isPrime(x: Int): Boolean {
        if (x < 2) return false
        run {
            var i = 2
            while (i * i <= x) {
                if (x % i == 0) return false
                i = i + 1
            }
        }
        return true
    }
}
