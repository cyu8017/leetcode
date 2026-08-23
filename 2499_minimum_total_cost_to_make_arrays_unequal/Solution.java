// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long minimumTotalCost(int[] nums1, int[] nums2) {
        int n = nums1.length;
        Map<Integer, Integer> freq = new HashMap<>();
        long ans = 0;
        int same = 0;
        for (int i = 0; i < n; i++) {
            if (nums1[i] == nums2[i]) {
                same++;
                freq.put(nums1[i], freq.getOrDefault(nums1[i], 0) + 1);
                ans += i;
            }
        }
        int maxFreq = 0, maxVal = 0;
        for (Map.Entry<Integer, Integer> kv : freq.entrySet()) {
            if (kv.getValue() > maxFreq) {
                maxFreq = kv.getValue();
                maxVal = kv.getKey();
            }
        }
        int need = maxFreq * 2 - same;
        if (need <= 0) return ans;
        for (int i = 0; i < n && need > 0; i++) {
            if (nums1[i] != nums2[i] && nums1[i] != maxVal && nums2[i] != maxVal) {
                ans += i;
                need--;
            }
        }
        return need > 0 ? -1 : ans;
    }
}
