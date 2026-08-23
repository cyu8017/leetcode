// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

import java.util.*;

class Solution {
    public int[][] averageHeightOfBuildings(int[][] buildings) {
        List<int[]> events = new ArrayList<>();
        for (int[] b : buildings) {
            events.add(new int[] { b[0], 1, b[2] });
            events.add(new int[] { b[1], -1, b[2] });
        }
        events.sort((a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        List<int[]> ans = new ArrayList<>();
        int count = 0, sum = 0, prev = events.get(0)[0];
        for (int[] e : events) {
            if (e[0] != prev && count > 0) {
                int avg = sum / count;
                if (!ans.isEmpty() && ans.get(ans.size() - 1)[1] == prev && ans.get(ans.size() - 1)[2] == avg)
                    ans.get(ans.size() - 1)[1] = e[0];
                else ans.add(new int[] { prev, e[0], avg });
            }
            count += e[1];
            sum += e[1] * e[2];
            prev = e[0];
        }
        return ans.toArray(new int[0][]);
    }
}
