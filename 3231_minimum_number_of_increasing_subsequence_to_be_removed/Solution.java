// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int minOperations(int[] nums) {
        var g = new ArrayList<Integer>();
        for (int x : nums) {
            int l = 0, r = g.size();
            while (l < r) {
                int mid = (l + r) >> 1;
                if (g.get(mid) < x) r = mid;
                else l = mid + 1;
            }
            if (l == g.size()) g.add(x);
            else g.set(l, x);
        }
        return g.size();
    }
}
