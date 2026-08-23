// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public long countGoodSubarrays(int[] nums) {
        int n = nums.length;
        var l = new int[n];
        Arrays.fill(l, -1);
        var stk = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (stk.size() > 0 && nums[stk.get(stk.size() - 1)] < x && (nums[stk.get(stk.size() - 1)] | x) == x) {
                stk.remove(stk.size() - 1);
            }
            if (stk.size() > 0) l[i] = stk.get(stk.size() - 1);
            stk.add(i);
        }
        var r = new int[n];
        Arrays.fill(r, n);
        stk.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (stk.size() > 0 && (nums[stk.get(stk.size() - 1)] | nums[i]) == nums[i]) {
                stk.remove(stk.size() - 1);
            }
            if (stk.size() > 0) r[i] = stk.get(stk.size() - 1);
            stk.add(i);
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += (long)(i - l[i]) * (r[i] - i);
        }
        return ans;
    }
}
