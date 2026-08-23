// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

using System.Collections.Generic;

public class Solution {
    public int MaxFrequency(int[] nums, int k) {
        int bas = 0;
        foreach (int x in nums) if (x == k) bas++;
        int ans = bas;
        var uniq = new HashSet<int>(nums);
        foreach (int v in uniq) {
            if (v == k) continue;
            int best = 0, cur = 0;
            foreach (int x in nums) {
                int delta = 0;
                if (x == v) delta = 1;
                else if (x == k) delta = -1;
                cur += delta;
                if (cur < 0) cur = 0;
                if (cur > best) best = cur;
            }
            if (bas + best > ans) ans = bas + best;
        }
        return ans;
    }
}
