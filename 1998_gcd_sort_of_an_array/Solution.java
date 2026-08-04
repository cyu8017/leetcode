// LeetCode 1998 - GCD Sort of an Array
// https://leetcode.com/problems/gcd-sort-of-an-array/

import java.util.*;

class Solution {
    int[] parent;

    public boolean gcdSort(int[] nums) {
        int m = 0;
        for (int x : nums) m = Math.max(m, x);
        parent = new int[m + 1];
        for (int i = 0; i <= m; i++) parent[i] = i;
        int[] spf = new int[m + 1];
        for (int i = 0; i <= m; i++) spf[i] = i;
        for (int i = 2; i * i <= m; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= m; j += i) if (spf[j] == j) spf[j] = i;
            }
        }
        Set<Integer> uniq = new HashSet<>();
        for (int x : nums) uniq.add(x);
        for (int x : uniq) {
            int y = x;
            while (y > 1) {
                int p = spf[y];
                union(x, p);
                while (y % p == 0) y /= p;
            }
        }
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        for (int i = 0; i < nums.length; i++) {
            if (find(nums[i]) != find(sorted[i])) return false;
        }
        return true;
    }

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra != rb) parent[rb] = ra;
    }
}
