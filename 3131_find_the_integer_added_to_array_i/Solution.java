// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

class Solution {
    public int addedInteger(int[] nums1, int[] nums2) {
        int min1 = nums1[0], min2 = nums2[0];
        for (int x : nums1) min1 = Math.min(min1, x);
        for (int x : nums2) min2 = Math.min(min2, x);
        return min2 - min1;
    }
}
