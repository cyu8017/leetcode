// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

public class Solution {
    public int XorBeauty(int[] nums) {
        int ans = 0;
        foreach (int x in nums) ans ^= x;
        return ans;
    }
}
