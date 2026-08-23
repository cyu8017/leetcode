// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int[] timeTaken(int[] arrival, int[] state) {
        int n = arrival.length;
        int[] ans = new int[n];
        Queue<Integer> enter = new ArrayDeque<>();
        Queue<Integer> exitq = new ArrayDeque<>();
        int i = 0, t = 0, prev = 1;
        while (i < n || !enter.isEmpty() || !exitq.isEmpty()) {
            while (i < n && arrival[i] <= t) {
                if (state[i] == 0) enter.offer(i);
                else exitq.offer(i);
                i++;
            }
            if (enter.isEmpty() && exitq.isEmpty()) {
                if (i < n) {
                    t = arrival[i];
                    prev = 1;
                }
                continue;
            }
            if (prev == 1) {
                if (!exitq.isEmpty()) {
                    ans[exitq.poll()] = t;
                    prev = 1;
                } else {
                    ans[enter.poll()] = t;
                    prev = 0;
                }
            } else {
                if (!enter.isEmpty()) {
                    ans[enter.poll()] = t;
                    prev = 0;
                } else {
                    ans[exitq.poll()] = t;
                    prev = 1;
                }
            }
            t++;
        }
        return ans;
    }
}
