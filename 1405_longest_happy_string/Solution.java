// LeetCode 1405 - Longest Happy String
// https://leetcode.com/problems/longest-happy-string/

import java.util.*;

class Solution {
    public String longestDiverseString(int a, int b, int c) {
        PriorityQueue<int[]> heap = new PriorityQueue<>((x, y) -> y[0] - x[0]);
        if (a > 0) heap.offer(new int[]{a, 'a'});
        if (b > 0) heap.offer(new int[]{b, 'b'});
        if (c > 0) heap.offer(new int[]{c, 'c'});
        StringBuilder answer = new StringBuilder();
        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int len = answer.length();
            if (len >= 2 && answer.charAt(len - 1) == cur[1] && answer.charAt(len - 2) == cur[1]) {
                if (heap.isEmpty()) break;
                int[] next = heap.poll();
                answer.append((char) next[1]);
                if (--next[0] > 0) heap.offer(next);
                heap.offer(cur);
            } else {
                answer.append((char) cur[1]);
                if (--cur[0] > 0) heap.offer(cur);
            }
        }
        return answer.toString();
    }
}
