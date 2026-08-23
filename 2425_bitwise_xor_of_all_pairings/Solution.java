// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        int ans = 0;
        if (nums2.length % 2 == 1) {
            for (int x : nums1) ans ^= x;
        }
        if (nums1.length % 2 == 1) {
            for (int x : nums2) ans ^= x;
        }
        return ans;
    }
}
