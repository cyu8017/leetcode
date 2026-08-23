// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

import java.util.*;

class Solution {
    public int brightestPosition(int[][] lights) {
        List<int[]> events = new ArrayList<>();
        for (int[] light : lights) {
            int pos = light[0], r = light[1];
            events.add(new int[] { pos - r, 1 });
            events.add(new int[] { pos + r + 1, -1 });
        }
        events.sort((a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(b[1], a[1]));
        int best = 0, cur = 0, ans = 0;
        for (int[] e : events) {
            cur += e[1];
            if (cur > best) { best = cur; ans = e[0]; }
        }
        return ans;
    }
}
