// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] delayedCount(int[] nums, int k) {
        int n = nums.length;
        Map<Integer, Integer> cnt = new HashMap<>();
        int[] ans = new int[n];
        for (int i = n - k - 2; i >= 0; i--) {
            int key = nums[i + k + 1];
            cnt.put(key, cnt.getOrDefault(key, 0) + 1);
            ans[i] = cnt.getOrDefault(nums[i], 0);
        }
        return ans;
    }
}
