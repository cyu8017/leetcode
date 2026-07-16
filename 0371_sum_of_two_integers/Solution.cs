// LeetCode 0371 - Sum of Two Integers

// https://leetcode.com/problems/sum-of-two-integers/



public class Solution {

    public int GetSum(int a, int b) {

        const uint mask = 0xFFFFFFFF;



        while (b != 0) {

            uint carry = (uint)((a & b) << 1);

            a = (int)(((uint)a ^ (uint)b) & mask);

            b = (int)(carry & mask);

        }



        return a <= 0x7FFFFFFF ? a : ~(a ^ (int)mask);

    }

}
