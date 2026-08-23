// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

using System.Collections.Generic;

public class Solution {
    public int CountNonDecreasingArrays(int[] digitSum) {
        const int mod = 1000000007;
        var groups = new List<int>[51];
        for (int i = 0; i <= 50; i++) groups[i] = new List<int>();
        for (int x = 0; x <= 5000; x++) {
            int s = 0;
            for (int y = x; y > 0; y /= 10) s += y % 10;
            groups[s].Add(x);
        }
        var prevVals = groups[digitSum[0]];
        var dp = new int[prevVals.Count];
        for (int i = 0; i < dp.Length; i++) dp[i] = 1;
        for (int pos = 1; pos < digitSum.Length; pos++) {
            var curVals = groups[digitSum[pos]];
            var next = new int[curVals.Count];
            int j = 0, prefix = 0;
            for (int i = 0; i < curVals.Count; i++) {
                int x = curVals[i];
                while (j < prevVals.Count && prevVals[j] <= x) {
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
        foreach (int x in dp) {
            ans += x;
            if (ans >= mod) ans -= mod;
        }
        return ans;
    }
}
