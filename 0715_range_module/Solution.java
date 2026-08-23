// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

import java.util.*;

class RangeModule {
    private List<int[]> intervals = new ArrayList<>();

    public RangeModule() {}

    public void addRange(int left, int right) {
        List<int[]> next = new ArrayList<>();
        boolean placed = false;
        for (int[] iv : intervals) {
            int start = iv[0], end = iv[1];
            if (end < left) next.add(new int[] {start, end});
            else if (right < start) {
                if (!placed) { next.add(new int[] {left, right}); placed = true; }
                next.add(new int[] {start, end});
            } else {
                left = Math.min(left, start);
                right = Math.max(right, end);
            }
        }
        if (!placed) next.add(new int[] {left, right});
        intervals = next;
    }

    public boolean queryRange(int left, int right) {
        for (int[] iv : intervals) {
            if (iv[0] <= left && right <= iv[1]) return true;
            if (iv[1] >= right) break;
        }
        return false;
    }

    public void removeRange(int left, int right) {
        List<int[]> next = new ArrayList<>();
        for (int[] iv : intervals) {
            int start = iv[0], end = iv[1];
            if (end <= left || right <= start) next.add(new int[] {start, end});
            else {
                if (start < left) next.add(new int[] {start, left});
                if (right < end) next.add(new int[] {right, end});
            }
        }
        intervals = next;
    }
}
