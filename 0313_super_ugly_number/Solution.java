// LeetCode 0313 - Super Ugly Number

// https://leetcode.com/problems/super-ugly-number/



class Solution {

    public int nthSuperUglyNumber(int n, int[] primes) {

        int[] ugly = new int[n];

        ugly[0] = 1;

        int[] pointers = new int[primes.length];

        for (int count = 1; count < n; count++) {

            int nextUgly = Integer.MAX_VALUE;

            for (int index = 0; index < primes.length; index++) {

                nextUgly = Math.min(nextUgly, ugly[pointers[index]] * primes[index]);

            }

            ugly[count] = nextUgly;

            for (int index = 0; index < primes.length; index++) {

                if (nextUgly == ugly[pointers[index]] * primes[index]) {

                    pointers[index]++;

                }

            }

        }

        return ugly[n - 1];

    }

}

