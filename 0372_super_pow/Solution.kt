// LeetCode 0372 - Super Pow

// https://leetcode.com/problems/super-pow/



class Solution {

    fun superPow(a: Int, b: IntArray): Int {

        val mod = 1337

        var base = a % mod

        var result = 1



        for (digit in b) {

            result = (powMod(result, 10, mod).toLong() * powMod(base, digit, mod) % mod).toInt()

        }



        return result

    }



    private fun powMod(base: Int, exponent: Int, mod: Int): Int {

        var currentBase = base

        var currentExponent = exponent

        var result = 1



        while (currentExponent > 0) {

            if (currentExponent and 1 == 1) {

                result = (result.toLong() * currentBase % mod).toInt()

            }

            currentBase = (currentBase.toLong() * currentBase % mod).toInt()

            currentExponent = currentExponent shr 1

        }



        return result

    }

}
