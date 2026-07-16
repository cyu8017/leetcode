// LeetCode 0390 - Elimination Game

// https://leetcode.com/problems/elimination-game/



class Solution {

    public int lastRemaining(int n) {

        int left = 1;

        int right = n;

        int step = 1;

        int remaining = n;

        boolean fromLeft = true;



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
