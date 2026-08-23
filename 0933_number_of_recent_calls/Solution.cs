// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

using System.Collections.Generic;

public class RecentCounter {
    private readonly Queue<int> q = new();

    public RecentCounter() {}

    public int Ping(int t) {
        q.Enqueue(t);
        while (q.Peek() < t - 3000) q.Dequeue();
        return q.Count;
    }
}
