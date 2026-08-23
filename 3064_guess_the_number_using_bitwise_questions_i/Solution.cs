// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

/**
 * Definition of commonSetBits API.
 * int CommonSetBits(int num);
 */

public class Solution : Guess {
    public int FindNumber() {
        int n = 0;
        for (int i = 0; i < 32; i++)
            if (CommonSetBits(1 << i) > 0) n |= 1 << i;
        return n;
    }
}
