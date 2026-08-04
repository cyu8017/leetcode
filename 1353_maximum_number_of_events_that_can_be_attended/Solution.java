// LeetCode 1353 - Maximum Number Of Events That Can Be Attended
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

import java.util.*;

class Solution {
    public int maxEvents(int[][] events) {
        Arrays.sort(events, Comparator.comparingInt(a -> a[0]));
        PriorityQueue<Integer> h = new PriorityQueue<>();
        int i = 0, ans = 0, day = 0, n = events.length;
        while (i < n || !h.isEmpty()) {
            if (h.isEmpty()) day = Math.max(day, events[i][0]);
            while (i < n && events[i][0] <= day) {
                h.offer(events[i][1]);
                i++;
            }
            while (!h.isEmpty() && h.peek() < day) h.poll();
            if (!h.isEmpty()) {
                h.poll();
                ans++;
                day++;
            }
        }
        return ans;
    }
}
