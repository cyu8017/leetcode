// LeetCode 2317 - Maximum XOR After Operations
// https://leetcode.com/problems/maximum-xor-after-operations/

class Solution {
    public int maximumXOR(int[] nums) {
        int ans = 0;
        for (int x : nums) ans |= x;
        return ans;
    }
}
