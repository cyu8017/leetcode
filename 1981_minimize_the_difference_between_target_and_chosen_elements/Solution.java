// LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

import java.util.*;

class Solution {
    public int minimizeTheDifference(int[][] mat, int target) {
        Set<Integer> possible = new HashSet<>();
        possible.add(0);
        for (int[] row : mat) {
            Set<Integer> uniq = new HashSet<>();
            for (int x : row) uniq.add(x);
            Set<Integer> nxt = new HashSet<>();
            for (int s : possible) for (int x : uniq) nxt.add(s + x);
            Set<Integer> kept = new HashSet<>();
            int minAbove = Integer.MAX_VALUE;
            for (int v : nxt) {
                if (v <= target) kept.add(v);
                else minAbove = Math.min(minAbove, v);
            }
            if (minAbove != Integer.MAX_VALUE) kept.add(minAbove);
            if (kept.isEmpty()) {
                int mn = Integer.MAX_VALUE;
                for (int v : nxt) mn = Math.min(mn, v);
                kept.add(mn);
            }
            possible = kept;
        }
        int ans = Integer.MAX_VALUE;
        for (int v : possible) ans = Math.min(ans, Math.abs(v - target));
        return ans;
    }
}
