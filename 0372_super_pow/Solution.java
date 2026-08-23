// LeetCode 0372 - Super Pow

// https://leetcode.com/problems/super-pow/



class Solution {

    public int superPow(int a, int[] b) {

        int mod = 1337;

        a %= mod;

        int result = 1;



        for (int digit : b) {

            result = powMod(result, 10, mod) * powMod(a, digit, mod) % mod;

        }



        return result;

    }



    private int powMod(int base, int exponent, int mod) {

        int result = 1;

        while (exponent > 0) {

            if ((exponent & 1) == 1) {

                result = (int) ((long) result * base % mod);

            }

            base = (int) ((long) base * base % mod);

            exponent >>= 1;

        }

        return result;

    }

}
