// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

class Solution {
    public int[] beautifulPair(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int best = Integer.MAX_VALUE;
        int[] ans = new int[] {0, 1};
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int d = Math.abs(nums1[i] - nums1[j]) + Math.abs(nums2[i] - nums2[j]);
                if (d < best || (d == best && (i < ans[0] || (i == ans[0] && j < ans[1])))) {
                    best = d;
                    ans = new int[] {i, j};
                }
            }
        }
        return ans;
    }
}
