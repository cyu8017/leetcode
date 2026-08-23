// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest_strictly_increasing_subsequence_with_non_zero_bitwise_and/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private static int bitLen(int x) {
        if (x == 0) return 0;
        int n = 0;
        while (x > 0) { n++; x >>= 1; }
        return n;
    }

    private static int lis(List<Integer> arr) {
        List<Integer> g = new ArrayList<>();
        for (int x : arr) {
            int idx = Collections.binarySearch(g, x);
            if (idx < 0) idx = ~idx;
            if (idx == g.size()) g.add(x);
            else g.set(idx, x);
        }
        return g.size();
    }

    public int longestSubsequence(int[] nums) {
        int ans = 0, mx = 0;
        for (int x : nums) mx = Math.max(mx, x);
        int m = bitLen(mx);
        for (int i = 0; i < m; i++) {
            List<Integer> arr = new ArrayList<>();
            for (int x : nums) {
                if (((x >> i) & 1) != 0) arr.add(x);
            }
            ans = Math.max(ans, lis(arr));
        }
        return ans;
    }
}
