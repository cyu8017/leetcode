// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

/**
 * Definition of commonBits API.
 * int CommonBits(int num);
 */

public class Solution : Guess {
    public int FindNumber() {
        int n = 0;
        for (int i = 0; i < 32; i++) {
            int count1 = CommonBits(1 << i);
            int count2 = CommonBits(1 << i);
            if (count1 > count2) n |= 1 << i;
        }
        return n;
    }
}
