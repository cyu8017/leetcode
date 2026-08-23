// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

import java.util.*;

class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] != b[1] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));
        int size = 0, first = -1, second = -1;
        for (int[] interval : intervals) {
            int left = interval[0], right = interval[1];
            if (left <= first) continue;
            if (left <= second) { size++; first = second; second = right; }
            else { size += 2; first = right - 1; second = right; }
        }
        return size;
    }
}
