// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

using System;
using System.Collections.Generic;

public class Solution {
    struct It {
        public int L, R, W, I;
    }
    class State {
        public long Score;
        public List<int> Idx = new List<int>();
    }

    static State Better(State a, State b) {
        if (a.Score != b.Score) return a.Score > b.Score ? a : b;
        for (int i = 0; i < a.Idx.Count && i < b.Idx.Count; i++) {
            if (a.Idx[i] != b.Idx[i]) return a.Idx[i] < b.Idx[i] ? a : b;
        }
        return a.Idx.Count <= b.Idx.Count ? a : b;
    }

    public int[] MaximumWeight(int[][] intervals) {
        int n = intervals.Length;
        var arr = new It[n];
        for (int i = 0; i < n; i++) arr[i] = new It { L = intervals[i][0], R = intervals[i][1], W = intervals[i][2], I = i };
        Array.Sort(arr, (a, b) => a.R.CompareTo(b.R));
        var dp = new State[n + 1][];
        for (int i = 0; i <= n; i++) {
            dp[i] = new State[5];
            for (int t = 0; t < 5; t++) dp[i][t] = new State();
        }
        for (int i = 1; i <= n; i++) {
            It cur = arr[i - 1];
            for (int t = 0; t <= 4; t++) {
                dp[i][t] = new State { Score = dp[i - 1][t].Score, Idx = new List<int>(dp[i - 1][t].Idx) };
            }
            int lo = 0, hi = i - 1;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (arr[mid].R < cur.L) lo = mid + 1;
                else hi = mid;
            }
            int prev = lo;
            for (int t = 1; t <= 4; t++) {
                State prevState = dp[prev][t - 1];
                var cand = new State();
                cand.Score = prevState.Score + cur.W;
                cand.Idx = new List<int>(prevState.Idx) { cur.I };
                cand.Idx.Sort();
                dp[i][t] = Better(dp[i][t], cand);
            }
        }
        State best = dp[n][0];
        for (int t = 1; t <= 4; t++) best = Better(best, dp[n][t]);
        return best.Idx.ToArray();
    }
}
