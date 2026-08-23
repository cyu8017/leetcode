// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

import java.util.Arrays;

class Solution {
    public int maxPossibleScore(int[] start, int d) {
        Arrays.sort(start);
        int n = start.length;
        int lo = 0, hi = start[n - 1] + d - start[0] + 1;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(start, d, mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    private boolean ok(int[] start, int d, int mid) {
        long prev = start[0];
        for (int i = 1; i < start.length; i++) {
            long need = prev + mid;
            long cur = start[i];
            if (need > cur + d) return false;
            prev = need > cur ? need : cur;
        }
        return true;
    }
}
