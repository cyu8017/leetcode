// LeetCode 0371 - Sum of Two Integers

// https://leetcode.com/problems/sum-of-two-integers/



class Solution {

    public int getSum(int a, int b) {

        int mask = 0xFFFFFFFF;



        while (b != 0) {

            int carry = (a & b) << 1;

            a = (a ^ b) & mask;

            b = carry & mask;

        }



        return a <= 0x7FFFFFFF ? a : ~(a ^ mask);

    }

}
