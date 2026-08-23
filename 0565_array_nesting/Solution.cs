// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/

public class Solution {
    public int ArrayNesting(int[] nums) {
        int best = 0;
        for (int i = 0; i < nums.Length; ++i) {
            if (nums[i] < 0) continue;
            int length = 0;
            int j = i;
            while (nums[j] >= 0) {
                int nxt = nums[j];
                nums[j] = -1;
                j = nxt;
                ++length;
            }
            if (length > best) best = length;
        }
        return best;
    }
}
