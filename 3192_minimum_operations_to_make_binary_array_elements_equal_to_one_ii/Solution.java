// LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

class Solution {
    public int minOperations(int[] nums) {
        int ans = 0, v = 0;
        for (int raw : nums) {
            int x = raw ^ v;
            if (x == 0) { v ^= 1; ans++; }
        }
        return ans;
    }
}
