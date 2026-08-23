// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public long maxScore(int[] nums) {
        var stk = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            while (stk.size() > 0 && nums[stk.get(stk.size() - 1)] <= nums[i]) stk.remove(stk.size() - 1);
            stk.add(i);
        }
        long ans = 0;
        int cur = 0;
        for (int j : stk) {
            ans += (long)(j - cur) * nums[j];
            cur = j;
        }
        return ans;
    }
}
