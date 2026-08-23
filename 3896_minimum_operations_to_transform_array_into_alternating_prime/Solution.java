// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private static final int MX = 200000;
    private static boolean[] isPrime;
    private static List<Integer> primes;
    private static boolean ready = false;

    private static void init() {
        if (ready) return;
        isPrime = new boolean[MX + 1];
        for (int i = 0; i <= MX; i++) isPrime[i] = true;
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i <= MX / i; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= MX; j += i) isPrime[j] = false;
            }
        }
        primes = new ArrayList<>();
        for (int i = 2; i <= MX; i++) if (isPrime[i]) primes.add(i);
        ready = true;
    }

    public int minOperations(int[] nums) {
        init();
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (i % 2 == 0) {
                int idx = Collections.binarySearch(primes, x);
                if (idx < 0) idx = ~idx;
                ans += primes.get(idx) - x;
            } else if (isPrime[x]) {
                ans += (x == 2) ? 2 : 1;
            }
        }
        return ans;
    }
}
