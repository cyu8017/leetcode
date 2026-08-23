// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

using System.Collections.Generic;

public class Solution {
    class Worker {
        public int Idx, Efficiency, LeftToRight, PickOld, RightToLeft, PutNew;
    }

    public int FindCrossingTime(int n, int k, int[][] time) {
        var left = new PriorityQueue<Worker, (int, int)>();
        var right = new PriorityQueue<Worker, (int, int)>();
        for (int i = 0; i < k; i++) {
            var w = new Worker {
                Idx = i,
                Efficiency = time[i][0] + time[i][2],
                LeftToRight = time[i][0],
                PickOld = time[i][1],
                RightToLeft = time[i][2],
                PutNew = time[i][3]
            };
            left.Enqueue(w, (-w.Efficiency, -w.Idx));
        }
        var events = new PriorityQueue<(int time, Worker w, int side), int>();
        int cur = 0, remain = n, done = 0, bridgeFree = 0;
        while (done < n) {
            while (events.Count > 0 && events.Peek().time <= cur) {
                var e = events.Dequeue();
                if (e.side == 0) left.Enqueue(e.w, (-e.w.Efficiency, -e.w.Idx));
                else right.Enqueue(e.w, (-e.w.Efficiency, -e.w.Idx));
            }
            if (cur < bridgeFree) {
                cur = bridgeFree;
                continue;
            }
            if (right.Count > 0) {
                var w = right.Dequeue();
                cur += w.RightToLeft;
                bridgeFree = cur;
                events.Enqueue((cur + w.PutNew, w, 0), cur + w.PutNew);
                done++;
                continue;
            }
            if (left.Count > 0 && remain > 0) {
                var w = left.Dequeue();
                cur += w.LeftToRight;
                bridgeFree = cur;
                remain--;
                events.Enqueue((cur + w.PickOld, w, 1), cur + w.PickOld);
                continue;
            }
            if (events.Count == 0) break;
            cur = events.Peek().time;
        }
        return cur;
    }
}
