// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

public class Solution {
    private class Fenwick {
        private readonly int[] bit;
        public Fenwick(int n) { bit = new int[n]; }
        public void Add(int i, int v) { for (; i < bit.Length; i += i & -i) bit[i] += v; }
        public int Sum(int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
    }

    public long GoodTriplets(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        int[] pos2 = new int[n], mapped = new int[n], left = new int[n], right = new int[n];
        for (int i = 0; i < n; i++) pos2[nums2[i]] = i;
        for (int i = 0; i < n; i++) mapped[i] = pos2[nums1[i]];
        var fw = new Fenwick(n + 2);
        for (int i = 0; i < n; i++) {
            left[i] = fw.Sum(mapped[i]);
            fw.Add(mapped[i] + 1, 1);
        }
        fw = new Fenwick(n + 2);
        for (int i = n - 1; i >= 0; i--) {
            right[i] = fw.Sum(n) - fw.Sum(mapped[i] + 1);
            fw.Add(mapped[i] + 1, 1);
        }
        long ans = 0;
        for (int i = 0; i < n; i++) ans += 1L * left[i] * right[i];
        return ans;
    }
}
