// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

import java.util.*;

class Solution {
    public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {
        List<Integer> tails = new ArrayList<>();
        int[] ans = new int[obstacles.length];
        for (int i = 0; i < obstacles.length; i++) {
            int x = obstacles[i];
            int idx = upperBound(tails, x);
            if (idx == tails.size()) tails.add(x);
            else tails.set(idx, x);
            ans[i] = idx + 1;
        }
        return ans;
    }

    private int upperBound(List<Integer> a, int x) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
