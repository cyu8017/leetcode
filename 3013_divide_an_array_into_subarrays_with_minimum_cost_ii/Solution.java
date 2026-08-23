// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

import java.util.Arrays;

class Solution {
    static class BITI {
        int n;
        int[] c;
        BITI(int n_) { n = n_; c = new int[n_ + 1]; }
        void upd(int x, int d) { for (; x <= n; x += x & -x) c[x] += d; }
        int qry(int x) { int s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    }
    static class BITL {
        int n;
        long[] c;
        BITL(int n_) { n = n_; c = new long[n_ + 1]; }
        void upd(int x, long d) { for (; x <= n; x += x & -x) c[x] += d; }
        long qry(int x) { long s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    }

    private static int kth(BITI cnt, int m, int k) {
        int idx = 0;
        for (int bit = 1 << 20; bit != 0; bit >>= 1) {
            int nidx = idx + bit;
            if (nidx <= m && cnt.c[nidx] < k) {
                k -= cnt.c[nidx];
                idx = nidx;
            }
        }
        return idx + 1;
    }

    public long minimumCost(int[] nums, int k, int dist) {
        k--;
        int n = nums.length;
        int[] uniq = nums.clone();
        Arrays.sort(uniq);
        int write = 0;
        for (int i = 0; i < uniq.length; i++)
            if (write == 0 || uniq[i] != uniq[write - 1]) uniq[write++] = uniq[i];
        uniq = Arrays.copyOf(uniq, write);
        int m = uniq.length;
        BITI cnt = new BITI(m + 2);
        BITL sum = new BITL(m + 2);
        for (int i = 1; i <= Math.min(dist + 1, n - 1); i++) {
            int r = Arrays.binarySearch(uniq, nums[i]);
            if (r < 0) r = -r - 1;
            r += 1;
            cnt.upd(r, 1);
            sum.upd(r, nums[i]);
        }
        int end = Math.min(dist + 1, n - 1);
        int kk = Math.min(k, end);
        long ans = nums[0] + sumSmallest(cnt, sum, uniq, m, kk);
        for (int i = dist + 2; i < n; i++) {
            int rem = nums[i - dist - 1];
            int r1 = Arrays.binarySearch(uniq, rem) + 1;
            cnt.upd(r1, -1);
            sum.upd(r1, -rem);
            int add = nums[i];
            int r2 = Arrays.binarySearch(uniq, add) + 1;
            cnt.upd(r2, 1);
            sum.upd(r2, add);
            kk = Math.min(k, dist + 1);
            ans = Math.min(ans, nums[0] + sumSmallest(cnt, sum, uniq, m, kk));
        }
        return ans;
    }

    private long sumSmallest(BITI cnt, BITL sum, int[] uniq, int m, int kk) {
        if (kk <= 0) return 0;
        int r = kth(cnt, m, kk);
        int before = cnt.qry(r - 1);
        long s = sum.qry(r - 1);
        s += (long) (kk - before) * uniq[r - 1];
        return s;
    }
}
