// LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
// https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

import java.util.ArrayList;
import java.util.List;

class Solution {
    boolean countInv(int[] nums, int k, int threshold) {
        var sorted = new ArrayList<Integer>();
        long inv = 0;
        for (int num : nums) {
            int left = upperBound(sorted, num);
            int right = upperBound(sorted, num + threshold);
            inv += right - left;
            sorted.add(upperBound(sorted, num), num);
        }
        return inv >= k;
    }
    static int upperBound(List<Integer> a, int target) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
    public int minThreshold(int[] nums, int k) {
        int mx = 0;
        for (int v : nums) if (v > mx) mx = v;
        int l = 0, r = mx + 1;
        while (l < r) {
            int m = (l + r) / 2;
            if (countInv(nums, k, m)) r = m;
            else l = m + 1;
        }
        return l > mx ? -1 : l;
    }
}
