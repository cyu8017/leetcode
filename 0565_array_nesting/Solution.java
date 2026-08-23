// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/

class Solution {
    public int arrayNesting(int[] nums) {
        int best = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] < 0) {
                continue;
            }
            int length = 0;
            int j = i;
            while (nums[j] >= 0) {
                int nxt = nums[j];
                nums[j] = -1;
                j = nxt;
                ++length;
            }
            best = Math.max(best, length);
        }
        return best;
    }
}
