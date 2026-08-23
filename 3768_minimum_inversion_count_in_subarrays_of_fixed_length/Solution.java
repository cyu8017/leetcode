// LeetCode 3768 - Minimum Inversion Count In Subarrays Of Fixed Length
// https://leetcode.com/problems/minimum_inversion_count_in_subarrays_of_fixed_length/

import java.util.Arrays;

class Solution {
    private int[] bit;

    public long minInversionCount(int[] nums, int k) {
        int[] vals = nums.clone();
        Arrays.sort(vals);
        int u = unique(vals);
        vals = Arrays.copyOf(vals, u);
        bit = new int[vals.length + 1];
        int[] rank = new int[nums.length];
        long inv = 0;
        for (int i = 0; i < nums.length; i++) {
            rank[i] = lowerBound(vals, nums[i]) + 1;
            if (i < k) {
                inv += i - sum(rank[i]);
                add(rank[i], 1);
            }
        }
        long best = inv;
        for (int r = k; r < nums.length; r++) {
            int left = rank[r - k];
            inv -= sum(left - 1);
            add(left, -1);
            inv += k - 1 - sum(rank[r]);
            add(rank[r], 1);
            if (inv < best) best = inv;
        }
        return best;
    }

    private void add(int i, int delta) {
        for (; i < bit.length; i += i & -i) bit[i] += delta;
    }

    private int sum(int i) {
        int res = 0;
        for (; i > 0; i -= i & -i) res += bit[i];
        return res;
    }

    private int unique(int[] a) {
        int n = 0;
        for (int i = 0; i < a.length; i++) {
            if (n == 0 || a[i] != a[n - 1]) a[n++] = a[i];
        }
        return n;
    }

    private int lowerBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
