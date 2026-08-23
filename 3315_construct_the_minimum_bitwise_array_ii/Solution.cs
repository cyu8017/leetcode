// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

using System.Collections.Generic;

public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        int[] ans = new int[nums.Count];
        for (int i = 0; i < nums.Count; i++) {
            ans[i] = -1;
            int n = nums[i];
            if (n == 2) continue;
            for (int b = 0; b < 31; b++) {
                if (((n >> b) & 1) == 0) continue;
                int x = n ^ (1 << b);
                if ((x | (x + 1)) == n) { ans[i] = x; break; }
            }
        }
        return ans;
    }
}
