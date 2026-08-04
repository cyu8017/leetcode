// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

import java.util.*;

class Solution {
    public int[][] removeInterval(int[][] intervals, int[] toBeRemoved) {
        int left = toBeRemoved[0], right = toBeRemoved[1];
        List<int[]> answer = new ArrayList<>();
        for (int[] interval : intervals) {
            int start = interval[0], end = interval[1];
            if (end <= left || start >= right) {
                answer.add(new int[] {start, end});
            } else {
                if (start < left) answer.add(new int[] {start, left});
                if (end > right) answer.add(new int[] {right, end});
            }
        }
        return answer.toArray(new int[0][]);
    }
}
