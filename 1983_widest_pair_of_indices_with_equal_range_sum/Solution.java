// LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
// https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

import java.util.*;

class Solution {
    public int widestPairOfIndices(int[] nums1, int[] nums2) {
        Map<Integer, Integer> first = new HashMap<>();
        first.put(0, -1);
        int ans = 0, s = 0;
        for (int i = 0; i < nums1.length; i++) {
            s += nums1[i] - nums2[i];
            if (first.containsKey(s)) ans = Math.max(ans, i - first.get(s));
            else first.put(s, i);
        }
        return ans;
    }
}
