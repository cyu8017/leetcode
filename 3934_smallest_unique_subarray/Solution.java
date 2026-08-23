// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/

import java.util.Arrays;

class Solution {
    public int smallestUniqueSubarray(int[] nums) {
        int n = nums.length;
        Integer[] sa = new Integer[n];
        int[] rank = Arrays.copyOf(nums, n);
        for (int i = 0; i < n; i++) sa[i] = i;
        for (int width = 1; width < n; width <<= 1) {
            final int w = width;
            final int[] r = rank;
            Arrays.sort(sa, (a, b) -> {
                if (r[a] != r[b]) return Integer.compare(r[a], r[b]);
                int ra = a + w < n ? r[a + w] : -1;
                int rb = b + w < n ? r[b + w] : -1;
                return Integer.compare(ra, rb);
            });
            int[] next = new int[n];
            for (int i = 1; i < n; i++) {
                int a = sa[i - 1], b = sa[i];
                boolean different = rank[a] != rank[b];
                int ra = a + width < n ? rank[a + width] : -1;
                int rb = b + width < n ? rank[b + width] : -1;
                next[b] = (different || ra != rb) ? next[a] + 1 : next[a];
            }
            rank = next;
            if (rank[sa[n - 1]] == n - 1) break;
        }
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) pos[sa[i]] = i;
        int[] lcp = new int[Math.max(0, n - 1)];
        int height = 0;
        for (int i = 0; i < n; i++) {
            int p = pos[i];
            if (p == n - 1) {
                height = 0;
                continue;
            }
            int j = sa[p + 1];
            while (i + height < n && j + height < n && nums[i + height] == nums[j + height]) height++;
            lcp[p] = height;
            if (height > 0) height--;
        }
        int ans = n;
        for (int p = 0; p < n; p++) {
            int start = sa[p];
            int need = 1;
            if (p > 0 && lcp[p - 1] + 1 > need) need = lcp[p - 1] + 1;
            if (p + 1 < n && lcp[p] + 1 > need) need = lcp[p] + 1;
            if (need <= n - start && need < ans) ans = need;
        }
        return ans;
    }
}
