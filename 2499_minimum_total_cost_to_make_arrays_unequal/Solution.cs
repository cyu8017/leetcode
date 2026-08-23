// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

using System.Collections.Generic;

public class Solution {
    public long MinimumTotalCost(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        var freq = new Dictionary<int, int>();
        long ans = 0;
        int same = 0;
        for (int i = 0; i < n; i++) {
            if (nums1[i] == nums2[i]) {
                same++;
                if (!freq.ContainsKey(nums1[i])) freq[nums1[i]] = 0;
                freq[nums1[i]]++;
                ans += i;
            }
        }
        int maxFreq = 0, maxVal = 0;
        foreach (var kv in freq) {
            if (kv.Value > maxFreq) {
                maxFreq = kv.Value;
                maxVal = kv.Key;
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
