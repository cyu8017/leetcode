// LeetCode 1389 - Create Target Array In The Given Order
// https://leetcode.com/problems/create-target-array-in-the-given-order/

import java.util.*;

class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        List<Integer> out = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) out.add(index[i], nums[i]);
        int[] ans = new int[out.size()];
        for (int i = 0; i < out.size(); i++) ans[i] = out.get(i);
        return ans;
    }
}
