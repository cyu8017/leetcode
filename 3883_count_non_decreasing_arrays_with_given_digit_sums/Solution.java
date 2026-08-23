// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int countNonDecreasingArrays(int[] digitSum) {
        final int mod = 1000000007;
        @SuppressWarnings("unchecked")
        List<Integer>[] groups = new ArrayList[51];
        for (int i = 0; i <= 50; i++) groups[i] = new ArrayList<>();
        for (int x = 0; x <= 5000; x++) {
            int s = 0;
            for (int y = x; y > 0; y /= 10) s += y % 10;
            groups[s].add(x);
        }
        List<Integer> prevVals = groups[digitSum[0]];
        int[] dp = new int[prevVals.size()];
        for (int i = 0; i < dp.length; i++) dp[i] = 1;
        for (int pos = 1; pos < digitSum.length; pos++) {
            List<Integer> curVals = groups[digitSum[pos]];
            int[] next = new int[curVals.size()];
            int j = 0, prefix = 0;
            for (int i = 0; i < curVals.size(); i++) {
                int x = curVals.get(i);
                while (j < prevVals.size() && prevVals.get(j) <= x) {
                    prefix += dp[j];
                    if (prefix >= mod) prefix -= mod;
                    j++;
                }
                next[i] = prefix;
            }
            prevVals = curVals;
            dp = next;
        }
        int ans = 0;
        for (int x : dp) {
            ans += x;
            if (ans >= mod) ans -= mod;
        }
        return ans;
    }
}
