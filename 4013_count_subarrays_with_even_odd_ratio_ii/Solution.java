// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

import java.util.Arrays;

class Solution {
    public long countRatioSubarrays(int[] nums, int a, int b) {
        int n = nums.length;
        long[] s = new long[n + 1];
        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 == 1) s[i + 1] = s[i] + a;
            else s[i + 1] = s[i] - b;
        }
        long[] st = s.clone();
        Arrays.sort(st);
        int uniq = 0;
        for (int i = 0; i < st.length; i++) {
            if (uniq == 0 || st[i] != st[uniq - 1]) st[uniq++] = st[i];
        }
        st = Arrays.copyOf(st, uniq);
        BIT bit = new BIT(st.length + 1);
        long ans = 0;
        for (long v : s) {
            int x = lowerBound(st, v) + 1;
            ans += bit.query(x);
            bit.update(x, 1);
        }
        return ans;
    }

    private int lowerBound(long[] a, long x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    static class BIT {
        int n;
        int[] c;
        BIT(int n) {
            this.n = n;
            c = new int[n + 1];
        }
        void update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        int query(int x) {
            int sum = 0;
            for (; x > 0; x -= x & -x) sum += c[x];
            return sum;
        }
    }
}
