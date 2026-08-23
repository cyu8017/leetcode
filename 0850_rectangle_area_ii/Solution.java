// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

import java.util.*;

class Solution {
    public int rectangleArea(int[][] rectangles) {
        final int MOD = 1_000_000_007;
        List<int[]> events = new ArrayList<>();
        for (int[] r : rectangles) {
            events.add(new int[] {r[0], 1, r[1], r[3]});
            events.add(new int[] {r[2], -1, r[1], r[3]});
        }
        events.sort(Comparator.comparingInt(a -> a[0]));
        List<int[]> active = new ArrayList<>();
        long area = 0;
        int prevX = events.get(0)[0];
        for (int[] e : events) {
            int x = e[0], typ = e[1], y1 = e[2], y2 = e[3];
            area += (long) coveredLength(active) * (x - prevX);
            if (typ == 1) active.add(new int[] {y1, y2});
            else {
                for (int i = 0; i < active.size(); i++) {
                    if (active.get(i)[0] == y1 && active.get(i)[1] == y2) {
                        active.remove(i);
                        break;
                    }
                }
            }
            prevX = x;
        }
        return (int) (area % MOD);
    }

    private int coveredLength(List<int[]> active) {
        if (active.isEmpty()) return 0;
        List<int[]> sorted = new ArrayList<>(active);
        sorted.sort(Comparator.comparingInt(a -> a[0]));
        int total = 0, curStart = sorted.get(0)[0], curEnd = sorted.get(0)[1];
        for (int i = 1; i < sorted.size(); i++) {
            int start = sorted.get(i)[0], end = sorted.get(i)[1];
            if (start > curEnd) {
                total += curEnd - curStart;
                curStart = start;
                curEnd = end;
            } else {
                curEnd = Math.max(curEnd, end);
            }
        }
        total += curEnd - curStart;
        return total;
    }
}
