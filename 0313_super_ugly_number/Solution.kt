// LeetCode 0313 - Super Ugly Number

// https://leetcode.com/problems/super-ugly-number/



class Solution {

    fun nthSuperUglyNumber(n: Int, primes: IntArray): Int {

        val ugly = IntArray(n)

        ugly[0] = 1

        val pointers = IntArray(primes.size)

        for (count in 1 until n) {

            var nextUgly = Int.MAX_VALUE

            for (index in primes.indices) {

                nextUgly = minOf(nextUgly, ugly[pointers[index]] * primes[index])

            }

            ugly[count] = nextUgly

            for (index in primes.indices) {

                if (nextUgly == ugly[pointers[index]] * primes[index]) {

                    pointers[index]++

                }

            }

        }

        return ugly[n - 1]

    }

}

