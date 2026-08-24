// LeetCode 0367 - Valid Perfect Square

// https://leetcode.com/problems/valid-perfect-square/



class Solution {

    fun isPerfectSquare(num: Int): Boolean {

        var left = 1L

        var right = num.toLong()



        while (left <= right) {

            val mid = left + (right - left) / 2

            val square = mid * mid

            when {

                square == num.toLong() -> return true

                square < num -> left = mid + 1

                else -> right = mid - 1

            }

        }



        return false

    }

}
