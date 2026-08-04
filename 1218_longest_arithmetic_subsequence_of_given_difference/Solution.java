// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

import java.util.*;

class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        Map<Integer, Integer> dp = new HashMap<>();
        int ans = 0;
        for (int x : arr) {
            int len = dp.getOrDefault(x - difference, 0) + 1;
            dp.put(x, len);
            ans = Math.max(ans, len);
        }
        return ans;
    }
}
