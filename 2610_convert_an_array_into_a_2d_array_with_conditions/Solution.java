// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();
        for (int x : nums) {
            int f = freq.getOrDefault(x, 0);
            if (f == ans.size()) ans.add(new ArrayList<>());
            ans.get(f).add(x);
            freq.put(x, f + 1);
        }
        return ans;
    }
}
