// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

import java.util.List;
import java.util.TreeSet;

class Solution {
    public int minAbsoluteDifference(List<Integer> nums, int x) {
        if (x == 0) {
            int ans0 = Integer.MAX_VALUE;
            for (int i = 1; i < nums.size(); i++)
                ans0 = Math.min(ans0, Math.abs(nums.get(i) - nums.get(i - 1)));
            return ans0;
        }
        int ans = Integer.MAX_VALUE;
        TreeSet<Integer> arr = new TreeSet<>();
        for (int i = x; i < nums.size(); i++) {
            arr.add(nums.get(i - x));
            int cur = nums.get(i);
            Integer ceil = arr.ceiling(cur);
            if (ceil != null) ans = Math.min(ans, ceil - cur);
            Integer floor = arr.floor(cur);
            if (floor != null) ans = Math.min(ans, cur - floor);
        }
        return ans;
    }
}
