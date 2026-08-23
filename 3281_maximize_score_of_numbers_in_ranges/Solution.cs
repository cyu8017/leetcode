// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

using System;

public class Solution {
    public int MaxPossibleScore(int[] start, int d) {
        Array.Sort(start);
        int n = start.Length;
        bool Ok(int mid) {
            long prev = start[0];
            for (int i = 1; i < n; i++) {
                long need = prev + mid;
                long cur = start[i];
                if (need > cur + d) return false;
                prev = need > cur ? need : cur;
            }
            return true;
        }
        int lo = 0, hi = start[n - 1] + d - start[0] + 1;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
