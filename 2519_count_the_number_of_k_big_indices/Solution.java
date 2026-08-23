// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    private static class Fenwick {
        private int[] bit;
        Fenwick(int n) { bit = new int[n + 2]; }
        void add(int i, int v) {
            for (; i < bit.length; i += i & -i) bit[i] += v;
        }
        int sum(int i) {
            int s = 0;
            for (; i > 0; i -= i & -i) s += bit[i];
            return s;
        }
    }

    public int kBigIndices(int[] nums, int k) {
        int n = nums.length;
        int[] uniq = nums.clone();
        Arrays.sort(uniq);
        int m = 0;
        for (int i = 0; i < uniq.length; i++) {
            if (i == 0 || uniq[i] != uniq[i - 1]) uniq[m++] = uniq[i];
        }
        Map<Integer, Integer> rank = new HashMap<>();
        for (int i = 0; i < m; i++) rank.put(uniq[i], i + 1);
        int[] left = new int[n], right = new int[n];
        Fenwick ft = new Fenwick(m);
        for (int i = 0; i < n; i++) {
            int r = rank.get(nums[i]);
            left[i] = ft.sum(r - 1);
            ft.add(r, 1);
        }
        ft = new Fenwick(m);
        for (int i = n - 1; i >= 0; i--) {
            int r = rank.get(nums[i]);
            right[i] = ft.sum(r - 1);
            ft.add(r, 1);
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] >= k && right[i] >= k) ans++;
        }
        return ans;
    }
}
