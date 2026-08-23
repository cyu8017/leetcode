// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int minOperations(List<Integer> nums, int k) {
        Set<Integer> need = new HashSet<>();
        for (int i = 1; i <= k; i++) need.add(i);
        for (int i = nums.size() - 1; i >= 0; i--) {
            need.remove(nums.get(i));
            if (need.isEmpty()) return nums.size() - i;
        }
        return nums.size();
    }
}
