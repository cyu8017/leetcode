// LeetCode 0371 - Sum of Two Integers

// https://leetcode.com/problems/sum-of-two-integers/



class Solution {

    fun getSum(a: Int, b: Int): Int {

        var x = a

        var y = b

        val mask = 0xFFFFFFFF.toInt()



        while (y != 0) {

            val carry = (x and y) shl 1

            x = (x xor y) and mask

            y = carry and mask

        }



        return if (x <= 0x7FFFFFFF) x else (x xor mask).inv()

    }

}
