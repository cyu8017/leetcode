// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

using System;
using System.Collections.Generic;

public class Solution {
    class BITI {
        public int n;
        public int[] c;
        public BITI(int n_) { n = n_; c = new int[n_ + 1]; }
        public void Upd(int x, int d) { for (; x <= n; x += x & -x) c[x] += d; }
        public int Qry(int x) { int s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    }
    class BITL {
        public int n;
        public long[] c;
        public BITL(int n_) { n = n_; c = new long[n_ + 1]; }
        public void Upd(int x, long d) { for (; x <= n; x += x & -x) c[x] += d; }
        public long Qry(int x) { long s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    }
    static int Kth(BITI cnt, int m, int k) {
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

    public long MinimumCost(int[] nums, int k, int dist) {
        k--;
        int n = nums.Length;
        var uniq = new List<int>(nums);
        uniq.Sort();
        int write = 0;
        for (int i = 0; i < uniq.Count; i++)
            if (write == 0 || uniq[i] != uniq[write - 1]) uniq[write++] = uniq[i];
        uniq.RemoveRange(write, uniq.Count - write);
        int m = uniq.Count;
        var cnt = new BITI(m + 2);
        var sum = new BITL(m + 2);
        void AddVal(int x, int d) {
            int r = uniq.BinarySearch(x);
            if (r < 0) r = ~r;
            r += 1;
            cnt.Upd(r, d);
            sum.Upd(r, (long)d * x);
        }
        long SumSmallest(int kk) {
            if (kk <= 0) return 0;
            int r = Kth(cnt, m, kk);
            int before = cnt.Qry(r - 1);
            long s = sum.Qry(r - 1);
            s += (long)(kk - before) * uniq[r - 1];
            return s;
        }
        int end = Math.Min(dist + 1, n - 1);
        for (int i = 1; i <= end; i++) AddVal(nums[i], 1);
        int kk = Math.Min(k, end);
        long ans = nums[0] + SumSmallest(kk);
        for (int i = dist + 2; i < n; i++) {
            AddVal(nums[i - dist - 1], -1);
            AddVal(nums[i], 1);
            kk = Math.Min(k, dist + 1);
            ans = Math.Min(ans, nums[0] + SumSmallest(kk));
        }
        return ans;
    }
}
