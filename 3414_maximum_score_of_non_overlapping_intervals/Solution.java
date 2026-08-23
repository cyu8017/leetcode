// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    private static class It {
        int l, r, w, i;
        It(int l, int r, int w, int i) { this.l = l; this.r = r; this.w = w; this.i = i; }
    }
    private static class State {
        long score;
        List<Integer> idx = new ArrayList<>();
        State() { this(0); }
        State(long score) { this.score = score; }
        State copy() {
            State s = new State(score);
            s.idx = new ArrayList<>(idx);
            return s;
        }
    }

    private State better(State a, State b) {
        if (a.score != b.score) return a.score > b.score ? a : b;
        int n = Math.min(a.idx.size(), b.idx.size());
        for (int i = 0; i < n; i++) {
            if (!a.idx.get(i).equals(b.idx.get(i))) return a.idx.get(i) < b.idx.get(i) ? a : b;
        }
        return a.idx.size() <= b.idx.size() ? a : b;
    }

    public int[] maximumWeight(int[][] intervals) {
        int n = intervals.length;
        It[] arr = new It[n];
        for (int i = 0; i < n; i++) arr[i] = new It(intervals[i][0], intervals[i][1], intervals[i][2], i);
        Arrays.sort(arr, (a, b) -> Integer.compare(a.r, b.r));
        State[][] dp = new State[n + 1][5];
        for (int i = 0; i <= n; i++) for (int t = 0; t <= 4; t++) dp[i][t] = new State();
        for (int i = 1; i <= n; i++) {
            It cur = arr[i - 1];
            for (int t = 0; t <= 4; t++) dp[i][t] = dp[i - 1][t].copy();
            int lo = 0, hi = i - 1;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (arr[mid].r < cur.l) lo = mid + 1;
                else hi = mid;
            }
            int prev = lo;
            for (int t = 1; t <= 4; t++) {
                State prevState = dp[prev][t - 1];
                State cand = prevState.copy();
                cand.score = prevState.score + cur.w;
                cand.idx.add(cur.i);
                Collections.sort(cand.idx);
                dp[i][t] = better(dp[i][t], cand);
            }
        }
        State best = dp[n][0];
        for (int t = 1; t <= 4; t++) best = better(best, dp[n][t]);
        int[] res = new int[best.idx.size()];
        for (int i = 0; i < best.idx.size(); i++) res[i] = best.idx.get(i);
        return res;
    }
}
