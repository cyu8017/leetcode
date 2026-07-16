// LeetCode 0313 - Super Ugly Number

// https://leetcode.com/problems/super-ugly-number/



public class Solution {

    public int NthSuperUglyNumber(int n, int[] primes) {

        int[] ugly = new int[n];

        ugly[0] = 1;

        int[] pointers = new int[primes.Length];

        for (int count = 1; count < n; count++) {

            int nextUgly = int.MaxValue;

            for (int index = 0; index < primes.Length; index++) {

                nextUgly = System.Math.Min(nextUgly, ugly[pointers[index]] * primes[index]);

            }

            ugly[count] = nextUgly;

            for (int index = 0; index < primes.Length; index++) {

                if (nextUgly == ugly[pointers[index]] * primes[index]) {

                    pointers[index]++;

                }

            }

        }

        return ugly[n - 1];

    }

}

