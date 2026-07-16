// LeetCode 0374 - Guess Number Higher or Lower

// https://leetcode.com/problems/guess-number-higher-or-lower/

// The guess API is patched by the test runner.



fun guess(num: Int): Int = 0



class Solution {

    fun guessNumber(n: Int): Int {

        var left = 1

        var right = n



        while (left <= right) {

            val mid = left + (right - left) / 2

            when (val result = guess(mid)) {

                0 -> return mid

                -1 -> right = mid - 1

                else -> left = mid + 1

            }

        }



        return left

    }

}
