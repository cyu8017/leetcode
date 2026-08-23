// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution {
    public int maxDistance(int[] nums1, int[] nums2) {
        int answer = 0;
        int j = 0;

        for (int i = 0; i < nums1.length; i++) {
            while (j < nums2.length && nums1[i] <= nums2[j]) {
                j++;
            }
            answer = Math.max(answer, j - i - 1);
        }

        return answer;
    }
}
