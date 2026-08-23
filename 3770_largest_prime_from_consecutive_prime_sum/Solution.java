// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest_prime_from_consecutive_prime_sum/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final int MX = 500000;
    private static final List<Integer> S = new ArrayList<>();
    static {
        boolean[] isPrime = new boolean[MX + 1];
        ArraysFill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= MX; i++) {
            if (isPrime[i]) {
                primes.add(i);
                if ((long) i * i <= MX) {
                    for (int j = i * i; j <= MX; j += i) isPrime[j] = false;
                }
            }
        }
        S.add(0);
        int t = 0;
        for (int x : primes) {
            t += x;
            if (t > MX) break;
            if (isPrime[t]) S.add(t);
        }
    }

    private static void ArraysFill(boolean[] a, boolean v) {
        for (int i = 0; i < a.length; i++) a[i] = v;
    }

    public int largestPrime(int n) {
        int lo = 0, hi = S.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (S.get(mid) <= n) lo = mid + 1;
            else hi = mid;
        }
        return S.get(lo - 1);
    }
}
