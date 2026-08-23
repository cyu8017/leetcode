// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

class Solution {
    private static class Fenwick {
        private final int[] bit;
        Fenwick(int n) { bit = new int[n]; }
        void add(int i, int v) { for (; i < bit.length; i += i & -i) bit[i] += v; }
        int sum(int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
    }

    public long goodTriplets(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[] pos2 = new int[n], mapped = new int[n], left = new int[n], right = new int[n];
        for (int i = 0; i < n; i++) pos2[nums2[i]] = i;
        for (int i = 0; i < n; i++) mapped[i] = pos2[nums1[i]];
        Fenwick fw = new Fenwick(n + 2);
        for (int i = 0; i < n; i++) {
            left[i] = fw.sum(mapped[i]);
            fw.add(mapped[i] + 1, 1);
        }
        fw = new Fenwick(n + 2);
        for (int i = n - 1; i >= 0; i--) {
            right[i] = fw.sum(n) - fw.sum(mapped[i] + 1);
            fw.add(mapped[i] + 1, 1);
        }
        long ans = 0;
        for (int i = 0; i < n; i++) ans += 1L * left[i] * right[i];
        return ans;
    }
}
