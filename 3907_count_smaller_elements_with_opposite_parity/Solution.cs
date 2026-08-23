// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

using System;

public class Solution {
    class BIT {
        int n;
        int[] c;
        public BIT(int n_) { n = n_; c = new int[n_ + 1]; }
        public void Update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        public int Query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    }

    public int[] CountSmallerOppositeParity(int[] nums) {
        int n = nums.Length;
        var sorted = (int[])nums.Clone();
        Array.Sort(sorted);
        int m = 0;
        for (int i = 0; i < sorted.Length; i++) {
            if (i == 0 || sorted[i] != sorted[i - 1]) sorted[m++] = sorted[i];
        }
        Array.Resize(ref sorted, m);
        var bits = new BIT[] { new BIT(m), new BIT(m) };
        var ans = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int x = Array.BinarySearch(sorted, nums[i]);
            if (x < 0) x = ~x;
            x++;
            ans[i] = bits[(nums[i] & 1) ^ 1].Query(x - 1);
            bits[nums[i] & 1].Update(x, 1);
        }
        return ans;
    }
}
