// LeetCode 0400 - Nth Digit

// https://leetcode.com/problems/nth-digit/



class Solution {

    public int findNthDigit(int n) {

        int digits = 1;

        int count = 9;

        int start = 1;



        while (n > (long) digits * count) {

            n -= digits * count;

            digits++;

            count *= 10;

            start *= 10;

        }



        int number = start + (n - 1) / digits;

        String numberText = String.valueOf(number);

        return numberText.charAt((n - 1) % digits) - '0';

    }

}
