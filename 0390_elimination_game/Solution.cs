// LeetCode 0390 - Elimination Game

// https://leetcode.com/problems/elimination-game/



public class Solution {

    public int LastRemaining(int n) {

        int left = 1;

        int right = n;

        int step = 1;

        int remaining = n;

        bool fromLeft = true;



        while (left < right) {

            if (fromLeft || remaining % 2 == 1) {

                left += step;

            }

            right -= step;

            step *= 2;

            remaining /= 2;

            fromLeft = !fromLeft;

        }



        return left;

    }

}
