// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

public class Solution {
    public int XorAllNums(int[] nums1, int[] nums2) {
        int ans = 0;
        if (nums2.Length % 2 == 1) {
            foreach (int x in nums1) ans ^= x;
        }
        if (nums1.Length % 2 == 1) {
            foreach (int x in nums2) ans ^= x;
        }
        return ans;
    }
}
