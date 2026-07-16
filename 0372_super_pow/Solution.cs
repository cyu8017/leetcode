// LeetCode 0372 - Super Pow

// https://leetcode.com/problems/super-pow/



public class Solution {

    public int SuperPow(int a, int[] b) {

        const int mod = 1337;

        a %= mod;

        int result = 1;



        foreach (int digit in b) {

            result = (int)((long)PowMod(result, 10, mod) * PowMod(a, digit, mod) % mod);

        }



        return result;

    }



    private static int PowMod(int baseValue, int exponent, int mod) {

        long result = 1;

        long baseLong = baseValue;



        while (exponent > 0) {

            if ((exponent & 1) == 1) {

                result = result * baseLong % mod;

            }

            baseLong = baseLong * baseLong % mod;

            exponent >>= 1;

        }



        return (int)result;

    }

}
