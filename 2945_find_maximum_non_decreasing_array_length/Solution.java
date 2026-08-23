// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int findMaximumLength(int[] nums) {
        int n = nums.length;
        long[] pref = new long[n + 1], last = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        int[] dp = new int[n + 1];
        List<long[]> dq = new ArrayList<>();
        dq.add(new long[]{0, 0});
        for (int i = 1; i <= n; i++) {
            while (dq.size() > 1 && dq.get(1)[1] <= pref[i]) dq.remove(0);
            int j = (int) dq.get(0)[0];
            dp[i] = dp[j] + 1;
            last[i] = pref[i] - pref[j];
            long val = pref[i] + last[i];
            while (!dq.isEmpty() && dq.get(dq.size() - 1)[1] >= val) dq.remove(dq.size() - 1);
            dq.add(new long[]{i, val});
        }
        return dp[n];
    }
}
