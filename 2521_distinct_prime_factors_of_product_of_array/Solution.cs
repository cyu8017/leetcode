// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

using System.Collections.Generic;

public class Solution {
    public int DistinctPrimeFactors(int[] nums) {
        var set = new HashSet<int>();
        foreach (int num in nums) {
            int x = num;
            for (int p = 2; p * p <= x; p++) {
                if (x % p == 0) {
                    set.Add(p);
                    while (x % p == 0) x /= p;
                }
            }
            if (x > 1) set.Add(x);
        }
        return set.Count;
    }
}
