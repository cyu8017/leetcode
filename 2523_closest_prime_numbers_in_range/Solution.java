// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] closestPrimes(int left, int right) {
        boolean[] isPrime = new boolean[right + 1];
        Arrays.fill(isPrime, true);
        if (right >= 0) isPrime[0] = false;
        if (right >= 1) isPrime[1] = false;
        for (int i = 2; i * i <= right; i++) {
            if (!isPrime[i]) continue;
            for (int j = i * i; j <= right; j += i) isPrime[j] = false;
        }
        List<Integer> primes = new ArrayList<>();
        for (int i = left; i <= right; i++) if (isPrime[i]) primes.add(i);
        if (primes.size() < 2) return new int[] {-1, -1};
        int bestDiff = Integer.MAX_VALUE;
        int[] best = new int[] {-1, -1};
        for (int i = 0; i + 1 < primes.size(); i++) {
            int d = primes.get(i + 1) - primes.get(i);
            if (d < bestDiff) {
                bestDiff = d;
                best = new int[] {primes.get(i), primes.get(i + 1)};
            }
        }
        return best;
    }
}
