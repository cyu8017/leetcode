// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

using System.Collections.Generic;

public class Solution {
    public int MinCost(int[] nums1, int[] nums2) {
        var cnt2 = new Dictionary<int, int>();
        foreach (int x in nums2) {
            if (!cnt2.ContainsKey(x)) cnt2[x] = 0;
            cnt2[x]++;
        }
        var cnt1 = new Dictionary<int, int>();
        foreach (int x in nums1) {
            if (cnt2.ContainsKey(x) && cnt2[x] > 0) cnt2[x]--;
            else {
                if (!cnt1.ContainsKey(x)) cnt1[x] = 0;
                cnt1[x]++;
            }
        }
        int ans = 0;
        foreach (var v in cnt1.Values) {
            if (v % 2 == 1) return -1;
            ans += v / 2;
        }
        foreach (var v in cnt2.Values) {
            if (v % 2 == 1) return -1;
        }
        return ans;
    }
}
