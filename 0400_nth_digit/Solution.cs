// LeetCode 0400 - Nth Digit

// https://leetcode.com/problems/nth-digit/



public class Solution {

    public int FindNthDigit(int n) {

        int remaining = n;

        int digits = 1;

        int count = 9;

        int start = 1;



        while (remaining > digits * count) {

            remaining -= digits * count;

            digits++;

            count *= 10;

            start *= 10;

        }



        int number = start + (remaining - 1) / digits;

        string numberText = number.ToString();

        return numberText[(remaining - 1) % digits] - '0';

    }

}
