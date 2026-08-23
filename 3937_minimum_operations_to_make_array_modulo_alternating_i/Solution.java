// LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

class Solution {
    public int minOperations(int[] nums, int k) {
        for (int i = 0; i < nums.length; i++) nums[i] %= k;
        int ans = Integer.MAX_VALUE;
        for (int x = 0; x < k; x++) {
            for (int y = 0; y < k; y++) {
                if (x == y) continue;
                int cnt = 0;
                for (int i = 0; i < nums.length; i++) {
                    int target = (i & 1) != 0 ? y : x;
                    int diff = Math.abs(target - nums[i]);
                    cnt += Math.min(diff, k - diff);
                }
                ans = Math.min(ans, cnt);
            }
        }
        return ans;
    }
}
