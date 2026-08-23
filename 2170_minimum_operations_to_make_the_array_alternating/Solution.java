// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

import java.util.*;

class Solution {
    private int[] top2(int[] nums, List<Integer> idxs) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int i : idxs) freq.merge(nums[i], 1, Integer::sum);
        int a = 0, ac = 0, b = 0, bc = 0;
        for (Map.Entry<Integer, Integer> kv : freq.entrySet()) {
            int v = kv.getKey(), c = kv.getValue();
            if (c > ac) { b = a; bc = ac; a = v; ac = c; }
            else if (c > bc) { b = v; bc = c; }
        }
        return new int[] {a, ac, b, bc};
    }

    public int minimumOperations(int[] nums) {
        int n = nums.length;
        if (n == 1) return 0;
        List<Integer> even = new ArrayList<>();
        List<Integer> odd = new ArrayList<>();
        for (int i = 0; i < n; i++) (i % 2 == 0 ? even : odd).add(i);
        int[] e = top2(nums, even);
        int[] o = top2(nums, odd);
        if (e[0] != o[0]) return n - e[1] - o[1];
        return Math.min(n - e[1] - o[3], n - e[3] - o[1]);
    }
}
