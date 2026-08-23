// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

using System;

public class Solution {
    public int MaximumCandies(int[] candies, long k) {
        int mx = 0;
        foreach (int c in candies) mx = Math.Max(mx, c);
        int lo = 0, hi = mx;
        bool Can(int mid) {
            if (mid == 0) return true;
            long cnt = 0;
            foreach (int c in candies) {
                cnt += c / mid;
                if (cnt >= k) return true;
            }
            return false;
        }
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
