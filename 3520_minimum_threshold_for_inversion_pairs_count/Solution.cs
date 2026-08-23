// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

using System.Collections.Generic;

public class Solution {
    bool CountInv(int[] nums, int k, int threshold) {
        var sorted = new List<int>();
        long inv = 0;
        foreach (int num in nums) {
            int left = UpperBound(sorted, num);
            int right = UpperBound(sorted, num + threshold);
            inv += right - left;
            sorted.Insert(UpperBound(sorted, num), num);
        }
        return inv >= k;
    }
    static int UpperBound(List<int> a, int target) {
        int lo = 0, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
    public int MinThreshold(int[] nums, int k) {
        int mx = 0;
        foreach (int v in nums) if (v > mx) mx = v;
        int l = 0, r = mx + 1;
        while (l < r) {
            int m = (l + r) / 2;
            if (CountInv(nums, k, m)) r = m;
            else l = m + 1;
        }
        return l > mx ? -1 : l;
    }
}
