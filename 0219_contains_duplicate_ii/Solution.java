// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> lastIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (lastIndex.containsKey(nums[i]) && i - lastIndex.get(nums[i]) <= k) {
                return true;
            }
            lastIndex.put(nums[i], i);
        }
        return false;
    }
}
