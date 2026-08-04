// LeetCode 1995 - Count Special Quadruplets
// https://leetcode.com/problems/count-special-quadruplets/

class Solution {
    public int countQuadruplets(int[] nums) {
        int n = nums.length, ans = 0;
        for (int a = 0; a < n; a++) {
            for (int b = a + 1; b < n; b++) {
                for (int c = b + 1; c < n; c++) {
                    int s = nums[a] + nums[b] + nums[c];
                    for (int d = c + 1; d < n; d++) if (nums[d] == s) ans++;
                }
            }
        }
        return ans;
    }
}
