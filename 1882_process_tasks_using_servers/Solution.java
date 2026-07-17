// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public int[] assignTasks(int[] servers, int[] tasks) {
        PriorityQueue<int[]> available = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });
        for (int i = 0; i < servers.length; i++) {
            available.offer(new int[] {servers[i], i});
        }

        PriorityQueue<long[]> busy = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        int[] answer = new int[tasks.length];
        long time = 0;

        for (int moment = 0; moment < tasks.length; moment++) {
            int task = tasks[moment];
            time = Math.max(time, moment);

            while (!busy.isEmpty() && busy.peek()[0] <= time) {
                long[] finished = busy.poll();
                available.offer(new int[] {(int) finished[1], (int) finished[2]});
            }

            while (available.isEmpty()) {
                time = busy.peek()[0];
                while (!busy.isEmpty() && busy.peek()[0] <= time) {
                    long[] finished = busy.poll();
                    available.offer(new int[] {(int) finished[1], (int) finished[2]});
                }
            }

            int[] server = available.poll();
            busy.offer(new long[] {time + task, server[0], server[1]});
            answer[moment] = server[1];
        }

        return answer;
    }
}
