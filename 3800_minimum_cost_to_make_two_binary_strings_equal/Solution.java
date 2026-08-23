// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

class Solution {
    public long minimumCost(String s, String t, int flipCost, int swapCost, int crossCost) {
        long[] diff = new long[2];
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) != t.charAt(i)) diff[s.charAt(i) - '0']++;
        }
        long ans = (diff[0] + diff[1]) * flipCost;
        long mx = Math.max(diff[0], diff[1]);
        long mn = Math.min(diff[0], diff[1]);
        ans = Math.min(ans, mn * swapCost + (mx - mn) * flipCost);
        long avg = (mx + mn) / 2;
        ans = Math.min(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost);
        return ans;
    }
}
