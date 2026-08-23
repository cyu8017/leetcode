// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

import java.util.*;

class Solution {
    public String reorganizeString(String s) {
        int[] freq = new int[26];
        for (char ch : s.toCharArray()) freq[ch - 'a']++;
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) heap.offer(new int[] {freq[i], i});
        }
        if (!heap.isEmpty() && heap.peek()[0] > (s.length() + 1) / 2) return "";
        StringBuilder result = new StringBuilder();
        while (heap.size() >= 2) {
            int[] x = heap.poll();
            int[] y = heap.poll();
            result.append((char) ('a' + x[1]));
            result.append((char) ('a' + y[1]));
            if (--x[0] > 0) heap.offer(x);
            if (--y[0] > 0) heap.offer(y);
        }
        if (!heap.isEmpty()) result.append((char) ('a' + heap.peek()[1]));
        return result.toString();
    }
}
