// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

import java.util.Arrays;

class Solution {
    static class BIT {
        int n;
        int[] c;
        BIT(int n_) { n = n_; c = new int[n_ + 1]; }
        void update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        int query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    }

    public int[] countSmallerOppositeParity(int[] nums) {
        int n = nums.length;
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        int m = 0;
        for (int i = 0; i < sorted.length; i++) {
            if (i == 0 || sorted[i] != sorted[i - 1]) sorted[m++] = sorted[i];
        }
        sorted = Arrays.copyOf(sorted, m);
        BIT[] bits = { new BIT(m), new BIT(m) };
        int[] ans = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int x = Arrays.binarySearch(sorted, nums[i]);
            if (x < 0) x = ~x;
            x++;
            ans[i] = bits[(nums[i] & 1) ^ 1].query(x - 1);
            bits[nums[i] & 1].update(x, 1);
        }
        return ans;
    }
}
