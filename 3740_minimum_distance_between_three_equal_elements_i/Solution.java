// LeetCode 3740 - Minimum Distance Between Three Equal Elements I
// https://leetcode.com/problems/minimum_distance_between_three_equal_elements_i/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int minimumDistance(int[] nums) {
        Map<Integer, List<Integer>> g = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            g.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        int inf = 1 << 30;
        int ans = inf;
        for (List<Integer> ls : g.values()) {
            int m = ls.size();
            for (int h = 0; h < m - 2; h++) {
                ans = Math.min(ans, (ls.get(h + 2) - ls.get(h)) * 2);
            }
        }
        return ans == inf ? -1 : ans;
    }
}
