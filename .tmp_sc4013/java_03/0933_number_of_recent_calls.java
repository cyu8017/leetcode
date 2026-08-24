// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

import java.util.*;

class RecentCounter {
    private final Queue<Integer> q = new ArrayDeque<>();

    public RecentCounter() {}

    public int ping(int t) {
        q.offer(t);
        while (q.peek() < t - 3000) q.poll();
        return q.size();
    }
}
