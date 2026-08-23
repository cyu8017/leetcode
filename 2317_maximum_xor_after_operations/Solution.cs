// LeetCode 2317 - Maximum XOR After Operations
// https://leetcode.com/problems/maximum-xor-after-operations/

public class Solution {
    public int MaximumXOR(int[] nums) {
        int ans = 0;
        foreach (int x in nums) ans |= x;
        return ans;
    }
}
