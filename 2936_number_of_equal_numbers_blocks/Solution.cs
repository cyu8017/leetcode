// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

using System.Collections.Generic;

public class Solution {
    public int BlockCount(IList<int> nums) {
        if (nums.Count == 0) return 0;
        int ans = 1;
        for (int i = 1; i < nums.Count; i++)
            if (nums[i] != nums[i - 1]) ans++;
        return ans;
    }
}
