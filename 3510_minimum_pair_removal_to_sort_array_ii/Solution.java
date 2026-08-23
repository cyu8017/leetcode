// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

import java.util.TreeSet;

class Solution {
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        int inv = 0, ans = 0;
        TreeSet<long[]> sl = new TreeSet<>((a, b) -> a[0] != b[0] ? Long.compare(a[0], b[0]) : Long.compare(a[1], b[1]));
        TreeSet<Integer> idx = new TreeSet<>();
        for (int i = 0; i < n; i++) idx.add(i);
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] > nums[i + 1]) inv++;
            sl.add(new long[] {nums[i] + nums[i + 1], i});
        }
        while (inv > 0) {
            ans++;
            long[] p = sl.pollFirst();
            int s = (int) p[0], i = (int) p[1];
            int j = idx.ceiling(i + 1);
            if (nums[i] > nums[j]) inv--;
            Integer h = idx.floor(i - 1);
            if (h != null) {
                if (nums[h] > nums[i]) inv--;
                sl.remove(new long[] {nums[h] + nums[i], h});
                if (nums[h] > s) inv++;
                sl.add(new long[] {nums[h] + s, h});
            }
            Integer k = idx.ceiling(j + 1);
            if (k != null) {
                if (nums[j] > nums[k]) inv--;
                sl.remove(new long[] {nums[j] + nums[k], j});
                if (s > nums[k]) inv++;
                sl.add(new long[] {s + nums[k], i});
            }
            nums[i] = s;
            idx.remove(j);
        }
        return ans;
    }
}
