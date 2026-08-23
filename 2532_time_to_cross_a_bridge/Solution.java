// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

import java.util.PriorityQueue;

class Solution {
    static class Worker {
        int idx, efficiency, leftToRight, pickOld, rightToLeft, putNew;
        Worker(int idx, int[] t) {
            this.idx = idx;
            leftToRight = t[0];
            pickOld = t[1];
            rightToLeft = t[2];
            putNew = t[3];
            efficiency = t[0] + t[2];
        }
    }

    public int findCrossingTime(int n, int k, int[][] time) {
        PriorityQueue<Worker> left = new PriorityQueue<>((a, b) -> {
            if (a.efficiency != b.efficiency) return Integer.compare(b.efficiency, a.efficiency);
            return Integer.compare(b.idx, a.idx);
        });
        PriorityQueue<Worker> right = new PriorityQueue<>((a, b) -> {
            if (a.efficiency != b.efficiency) return Integer.compare(b.efficiency, a.efficiency);
            return Integer.compare(b.idx, a.idx);
        });
        Worker[] ws = new Worker[k];
        for (int i = 0; i < k; i++) {
            ws[i] = new Worker(i, time[i]);
            left.offer(ws[i]);
        }
        PriorityQueue<long[]> events = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        long cur = 0, bridgeFree = 0;
        int remain = n, done = 0;
        while (done < n) {
            while (!events.isEmpty() && events.peek()[0] <= cur) {
                long[] e = events.poll();
                Worker w = ws[(int) e[2]];
                if ((int) e[1] == 0) left.offer(w);
                else right.offer(w);
            }
            if (cur < bridgeFree) {
                cur = bridgeFree;
                continue;
            }
            if (!right.isEmpty()) {
                Worker w = right.poll();
                cur += w.rightToLeft;
                bridgeFree = cur;
                events.offer(new long[] {cur + w.putNew, 0, w.idx});
                done++;
                continue;
            }
            if (!left.isEmpty() && remain > 0) {
                Worker w = left.poll();
                cur += w.leftToRight;
                bridgeFree = cur;
                remain--;
                events.offer(new long[] {cur + w.pickOld, 1, w.idx});
                continue;
            }
            if (events.isEmpty()) break;
            cur = events.peek()[0];
        }
        return (int) cur;
    }
}
