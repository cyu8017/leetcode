// LeetCode 0343 - Integer Break

// https://leetcode.com/problems/integer-break/



public class Solution {

    public int IntegerBreak(int n) {

        if (n <= 3) {

            return n - 1;

        }



        int product = 1;

        while (n > 4) {

            product *= 3;

            n -= 3;

        }

        return product * n;

    }

}
