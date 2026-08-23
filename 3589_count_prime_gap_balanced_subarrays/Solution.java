// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int primeSubarray(int[] nums, int k) {
        int mx = 0;
        for (int v : nums) mx = Math.max(mx, v);
        boolean[] isPrime = new boolean[mx + 1];
        for (int i = 2; i <= mx; i++) isPrime[i] = true;
        for (int i = 2; i * i <= mx; i++)
            if (isPrime[i])
                for (int j = i * i; j <= mx; j += i) isPrime[j] = false;
        int n = nums.length, ans = 0;
        for (int l = 0; l < n; l++) {
            var primes = new ArrayList<Integer>();
            for (int r = l; r < n; r++) {
                if (isPrime[nums[r]]) primes.add(nums[r]);
                if (primes.size() >= 2) {
                    int mn = primes.get(0), mxp = primes.get(0);
                    for (int p : primes) {
                        mn = Math.min(mn, p);
                        mxp = Math.max(mxp, p);
                    }
                    if (mxp - mn <= k) ans++;
                }
            }
        }
        return ans;
    }
}
