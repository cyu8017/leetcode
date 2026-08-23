// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge_adjacent_equal_elements/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public long[] mergeAdjacent(int[] nums) {
        List<Long> stk = new ArrayList<>();
        for (int x : nums) {
            stk.add((long) x);
            while (stk.size() > 1 && stk.get(stk.size() - 1).equals(stk.get(stk.size() - 2))) {
                long a = stk.remove(stk.size() - 1);
                long b = stk.remove(stk.size() - 1);
                stk.add(a + b);
            }
        }
        long[] ans = new long[stk.size()];
        for (int i = 0; i < stk.size(); i++) ans[i] = stk.get(i);
        return ans;
    }
}
