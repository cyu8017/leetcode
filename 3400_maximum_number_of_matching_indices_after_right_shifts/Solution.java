// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

class Solution {
    public int maximumMatchingIndices(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int ans = 0;
        for (int shift = 0; shift < n; shift++) {
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (nums1[(i - shift + n) % n] == nums2[i]) cnt++;
            }
            if (cnt > ans) ans = cnt;
        }
        return ans;
    }
}
