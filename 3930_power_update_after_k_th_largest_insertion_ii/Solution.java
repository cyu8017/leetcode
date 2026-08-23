// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

import java.util.Arrays;

class Solution {
    public int[] powerUpdate(int[] nums, int p, int[][] queries) {
        final long mod = 1000000007;
        int[] vals = Arrays.copyOf(nums, nums.length + queries.length);
        for (int i = 0; i < queries.length; i++) vals[nums.length + i] = queries[i][0];
        Arrays.sort(vals);
        int uniq = 0;
        for (int i = 0; i < vals.length; i++) {
            if (uniq == 0 || vals[i] != vals[uniq - 1]) vals[uniq++] = vals[i];
        }
        vals = Arrays.copyOf(vals, uniq);
        int[] bit = new int[vals.length + 1];
        for (int x : nums) add(bit, lowerBound(vals, x) + 1);
        int[] ans = new int[queries.length];
        int size = nums.length;
        long cur = p;
        for (int i = 0; i < queries.length; i++) {
            add(bit, lowerBound(vals, queries[i][0]) + 1);
            size++;
            int x = kth(bit, vals, size - queries[i][1] + 1);
            cur = powm(cur, x, mod);
            ans[i] = (int) cur;
        }
        return ans;
    }

    private void add(int[] bit, int i) {
        for (; i < bit.length; i += i & -i) bit[i]++;
    }

    private int kth(int[] bit, int[] vals, int rank) {
        int idx = 0;
        int step = 1;
        while ((step << 1) < bit.length) step <<= 1;
        for (; step > 0; step >>= 1) {
            int next = idx + step;
            if (next < bit.length && bit[next] < rank) {
                idx = next;
                rank -= bit[next];
            }
        }
        return vals[idx];
    }

    private int lowerBound(int[] vals, int x) {
        int lo = 0, hi = vals.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (vals[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    private long powm(long a, long e, long mod) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return res;
    }
}
