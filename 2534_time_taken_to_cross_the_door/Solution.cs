// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

using System.Collections.Generic;

public class Solution {
    public int[] TimeTaken(int[] arrival, int[] state) {
        int n = arrival.Length;
        int[] ans = new int[n];
        var enter = new Queue<int>();
        var exitq = new Queue<int>();
        int i = 0, t = 0, prev = 1;
        while (i < n || enter.Count > 0 || exitq.Count > 0) {
            while (i < n && arrival[i] <= t) {
                if (state[i] == 0) enter.Enqueue(i);
                else exitq.Enqueue(i);
                i++;
            }
            if (enter.Count == 0 && exitq.Count == 0) {
                if (i < n) {
                    t = arrival[i];
                    prev = 1;
                }
                continue;
            }
            if (prev == 1) {
                if (exitq.Count > 0) {
                    ans[exitq.Dequeue()] = t;
                    prev = 1;
                } else {
                    ans[enter.Dequeue()] = t;
                    prev = 0;
                }
            } else {
                if (enter.Count > 0) {
                    ans[enter.Dequeue()] = t;
                    prev = 0;
                } else {
                    ans[exitq.Dequeue()] = t;
                    prev = 1;
                }
            }
            t++;
        }
        return ans;
    }
}
