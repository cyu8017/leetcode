// LeetCode 1349 - Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/

import java.util.*;

class Solution {
    public int maxStudents(char[][] seats) {
        int rows = seats.length, cols = seats[0].length;
        List<List<Integer>> validRows = new ArrayList<>();
        for (char[] row : seats) {
            int available = 0;
            for (int c = 0; c < cols; c++) if (row[c] == '.') available |= 1 << c;
            List<Integer> masks = new ArrayList<>();
            for (int mask = 0; mask < (1 << cols); mask++) {
                if ((mask & ~available) == 0 && (mask & (mask << 1)) == 0) masks.add(mask);
            }
            validRows.add(masks);
        }
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 0);
        for (List<Integer> masks : validRows) {
            Map<Integer, Integer> nxt = new HashMap<>();
            for (int mask : masks) {
                for (Map.Entry<Integer, Integer> e : dp.entrySet()) {
                    int previous = e.getKey(), count = e.getValue();
                    if ((mask & (previous << 1)) == 0 && (mask & (previous >> 1)) == 0) {
                        nxt.merge(mask, count + Integer.bitCount(mask), Math::max);
                    }
                }
            }
            dp = nxt;
        }
        int ans = 0;
        for (int v : dp.values()) ans = Math.max(ans, v);
        return ans;
    }
}
