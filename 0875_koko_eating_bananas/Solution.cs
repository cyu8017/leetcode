// LeetCode 0875 - Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

using System;

public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        int lo = 1, hi = 0;
        foreach (int p in piles) hi = Math.Max(hi, p);
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long hours = 0;
            foreach (int p in piles) hours += (p + mid - 1) / mid;
            if (hours <= h) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
