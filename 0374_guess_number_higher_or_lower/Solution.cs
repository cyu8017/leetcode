// LeetCode 0374 - Guess Number Higher or Lower

// https://leetcode.com/problems/guess-number-higher-or-lower/

// The guess API is patched by the test runner.



public class Solution {

    protected int Guess(int num) {

        return 0;

    }



    public int GuessNumber(int n) {

        int left = 1;

        int right = n;



        while (left <= right) {

            int mid = left + (right - left) / 2;

            int result = Guess(mid);

            if (result == 0) {

                return mid;

            }

            if (result < 0) {

                right = mid - 1;

            } else {

                left = mid + 1;

            }

        }



        return left;

    }

}
