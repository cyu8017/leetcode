// LeetCode 0390 - Elimination Game

// https://leetcode.com/problems/elimination-game/



class Solution {

    fun lastRemaining(n: Int): Int {

        var left = 1

        var right = n

        var step = 1

        var remaining = n

        var fromLeft = true



        while (left < right) {

            if (fromLeft || remaining % 2 == 1) {

                left += step

            }

            right -= step

            step *= 2

            remaining /= 2

            fromLeft = !fromLeft

        }



        return left

    }

}
