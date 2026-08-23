// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

using System.Collections.Generic;

public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        int[] ans = new int[nums.Count];
        for (int i = 0; i < nums.Count; i++) {
            ans[i] = -1;
            for (int x = 0; x < nums[i]; x++) {
                if ((x | (x + 1)) == nums[i]) { ans[i] = x; break; }
            }
        }
        return ans;
    }
}
