// LeetCode 0397 - Integer Replacement

// https://leetcode.com/problems/integer-replacement/



public class Solution {

    public int IntegerReplacement(int n) {

        long value = n;

        int steps = 0;



        while (value != 1) {

            if (value % 2 == 0) {

                value /= 2;

            } else if (value == 3 || value % 4 == 1) {

                value -= 1;

            } else {

                value += 1;

            }

            steps++;

        }



        return steps;

    }

}
