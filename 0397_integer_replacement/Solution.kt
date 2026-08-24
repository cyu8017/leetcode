// LeetCode 0397 - Integer Replacement

// https://leetcode.com/problems/integer-replacement/



class Solution {

    fun integerReplacement(n: Int): Int {

        var value = n.toLong()

        var steps = 0



        while (value != 1L) {

            when {

                value % 2L == 0L -> value /= 2

                value == 3L || value % 4L == 1L -> value -= 1

                else -> value += 1

            }

            steps++

        }



        return steps

    }

}
