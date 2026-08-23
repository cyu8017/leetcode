// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int distinctPrimeFactors(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            int x = num;
            for (int p = 2; p * p <= x; p++) {
                if (x % p == 0) {
                    set.add(p);
                    while (x % p == 0) x /= p;
                }
            }
            if (x > 1) set.add(x);
        }
        return set.size();
    }
}
