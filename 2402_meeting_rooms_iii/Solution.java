// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<Long> free = new PriorityQueue<>();
        for (int i = 0; i < n; i++) free.offer((long) i);
        PriorityQueue<long[]> busy = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return Long.compare(a[0], b[0]);
            return Long.compare(a[1], b[1]);
        });
        int[] cnt = new int[n];
        for (int[] m : meetings) {
            long start = m[0], end = m[1];
            while (!busy.isEmpty() && busy.peek()[0] <= start) {
                free.offer(busy.poll()[1]);
            }
            long dur = end - start;
            long room, begin;
            if (!free.isEmpty()) {
                room = free.poll();
                begin = start;
            } else {
                long[] top = busy.poll();
                begin = top[0];
                room = top[1];
            }
            busy.offer(new long[] {begin + dur, room});
            cnt[(int) room]++;
        }
        int ans = 0;
        for (int i = 1; i < n; i++) {
            if (cnt[i] > cnt[ans]) ans = i;
        }
        return ans;
    }
}
