// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution {
    fun countPrimeSetBits(left: Int, right: Int): Int {
        val primes = hashSetOf(2, 3, 5, 7, 11, 13, 17, 19)
        var ans = 0
        for (num in left..right) {
            if (num.countOneBits() in primes) ans++
        }
        return ans
    }
}
