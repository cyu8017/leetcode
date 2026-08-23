// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution {
    public int xorBeauty(int[] nums) {
        int ans = 0;
        for (int x : nums) ans ^= x;
        return ans;
    }
}
