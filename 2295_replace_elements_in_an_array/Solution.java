// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] arrayChange(int[] nums, int[][] operations) {
        var pos = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) pos.put(nums[i], i);
        for (var op : operations) {
            int i = pos.get(op[0]);
            nums[i] = op[1];
            pos.remove(op[0]);
            pos.put(op[1], i);
        }
        return nums;
    }
}
