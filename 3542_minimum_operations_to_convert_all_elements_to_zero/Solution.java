// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int minOperations(int[] nums) {
        var stk = new ArrayList<Integer>();
        int ans = 0;
        for (int x : nums) {
            while (stk.size() > 0 && stk.get(stk.size() - 1) > x) {
                ans++;
                stk.remove(stk.size() - 1);
            }
            if (x != 0 && (stk.size() == 0 || stk.get(stk.size() - 1) != x)) stk.add(x);
        }
        ans += stk.size();
        return ans;
    }
}
