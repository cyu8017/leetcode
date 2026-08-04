// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

import java.util.*;

class Solution {
    public List<Integer> longestCommonSubsequence(int[][] arrays) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int[] arr : arrays) for (int x : arr) cnt.merge(x, 1, Integer::sum);
        List<Integer> ans = new ArrayList<>();
        int m = arrays.length;
        for (int x : arrays[0]) if (cnt.get(x) == m) ans.add(x);
        return ans;
    }
}
