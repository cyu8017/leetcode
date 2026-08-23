// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution {
    public boolean uniformArray(int[] nums1) {
        int mn = Integer.MAX_VALUE;
        for (int x : nums1) {
            if (x % 2 == 1 && x < mn) mn = x;
        }
        for (int x : nums1) {
            if (x % 2 == 0 && mn != Integer.MAX_VALUE && x < mn) return false;
        }
        return true;
    }
}
