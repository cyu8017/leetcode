// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

class Solution {
    private static final int M = 31623;
    private static boolean[] primes;
    private static boolean inited;

    private static void initPrimes() {
        if (inited) return;
        primes = new boolean[M + 1];
        for (int i = 0; i <= M; i++) primes[i] = true;
        primes[0] = primes[1] = false;
        for (int i = 2; i <= M; i++) {
            if (primes[i]) {
                for (int j = i * 2; j <= M; j += i) primes[j] = false;
            }
        }
        inited = true;
    }

    public int nonSpecialCount(int l, int r) {
        initPrimes();
        int lo = (int) Math.ceil(Math.sqrt(l));
        int hi = (int) Math.floor(Math.sqrt(r));
        int cnt = 0;
        for (int i = lo; i <= hi; i++) {
            if (primes[i]) cnt++;
        }
        return r - l + 1 - cnt;
    }
}
