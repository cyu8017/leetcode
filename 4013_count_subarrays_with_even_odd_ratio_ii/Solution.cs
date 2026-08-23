// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

using System;
using System.Collections.Generic;

public class Solution {
    class BIT {
        int n;
        int[] c;
        public BIT(int n_) { n = n_; c = new int[n_ + 1]; }
        public void Update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        public int Query(int x) {
            int sum = 0;
            for (; x > 0; x -= x & -x) sum += c[x];
            return sum;
        }
    }

    public long CountRatioSubarrays(int[] nums, int a, int b) {
        int n = nums.Length;
        long[] s = new long[n + 1];
        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 == 1) s[i + 1] = s[i] + a;
            else s[i + 1] = s[i] - b;
        }
        var st = new List<long>(s);
        st.Sort();
        int w = 0;
        for (int i = 0; i < st.Count; i++) {
            if (i == 0 || st[i] != st[i - 1]) st[w++] = st[i];
        }
        st.RemoveRange(w, st.Count - w);
        var bit = new BIT(st.Count + 1);
        long ans = 0;
        foreach (long v in s) {
            int lo = 0, hi = st.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (st[mid] < v) lo = mid + 1;
                else hi = mid;
            }
            int x = lo + 1;
            ans += bit.Query(x);
            bit.Update(x, 1);
        }
        return ans;
    }
}
