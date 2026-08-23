// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

import java.util.*;

class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        int less = 0, eq = 0;
        for (int x : nums) {
            if (x < target) less++;
            else if (x == target) eq++;
        }
        List<Integer> ans = new ArrayList<>(eq);
        for (int i = 0; i < eq; i++) ans.add(less + i);
        return ans;
    }
}
