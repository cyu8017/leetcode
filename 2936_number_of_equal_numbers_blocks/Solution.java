// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

import java.util.List;

class Solution {
    public int blockCount(List<Integer> nums) {
        if (nums.isEmpty()) return 0;
        int ans = 1;
        for (int i = 1; i < nums.size(); i++)
            if (!nums.get(i).equals(nums.get(i - 1))) ans++;
        return ans;
    }
}
