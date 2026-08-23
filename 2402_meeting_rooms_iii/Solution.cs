// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

using System;
using System.Collections.Generic;

public class Solution {
    public int MostBooked(int n, int[][] meetings) {
        Array.Sort(meetings, (a, b) => a[0].CompareTo(b[0]));
        var free = new PriorityQueue<long, long>();
        for (int i = 0; i < n; i++) free.Enqueue(i, i);
        var busy = new PriorityQueue<(long end, long room), (long end, long room)>();
        int[] cnt = new int[n];
        foreach (var m in meetings) {
            long start = m[0], end = m[1];
            while (busy.Count > 0 && busy.Peek().end <= start) {
                var top = busy.Dequeue();
                free.Enqueue(top.room, top.room);
            }
            long dur = end - start;
            long room, begin;
            if (free.Count > 0) {
                room = free.Dequeue();
                begin = start;
            } else {
                var top = busy.Dequeue();
                begin = top.end;
                room = top.room;
            }
            busy.Enqueue((begin + dur, room), (begin + dur, room));
            cnt[room]++;
        }
        int ans = 0;
        for (int i = 1; i < n; i++) if (cnt[i] > cnt[ans]) ans = i;
        return ans;
    }
}
