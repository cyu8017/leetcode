// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minCost(int[] nums1, int[] nums2) {
        Map<Integer, Integer> cnt2 = new HashMap<>();
        for (int x : nums2) cnt2.put(x, cnt2.getOrDefault(x, 0) + 1);
        Map<Integer, Integer> cnt1 = new HashMap<>();
        for (int x : nums1) {
            int c = cnt2.getOrDefault(x, 0);
            if (c > 0) cnt2.put(x, c - 1);
            else cnt1.put(x, cnt1.getOrDefault(x, 0) + 1);
        }
        int ans = 0;
        for (int v : cnt1.values()) {
            if (v % 2 == 1) return -1;
            ans += v / 2;
        }
        for (int v : cnt2.values()) {
            if (v % 2 == 1) return -1;
        }
        return ans;
    }
}
