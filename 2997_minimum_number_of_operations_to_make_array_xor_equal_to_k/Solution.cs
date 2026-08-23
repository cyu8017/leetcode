// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

public class Solution {
    public int MinOperations(int[] nums, int k) {
        int xorr = 0;
        foreach (int v in nums) xorr ^= v;
        int diff = xorr ^ k;
        int ans = 0;
        while (diff > 0) {
            ans += diff & 1;
            diff >>= 1;
        }
        return ans;
    }
}
