// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

import java.util.ArrayList;
import java.util.List;

class MRUQueue {
    private final List<Integer> q = new ArrayList<>();

    public MRUQueue(int n) {
        for (int i = 1; i <= n; i++) {
            q.add(i);
        }
    }

    public int fetch(int k) {
        int val = q.remove(k - 1);
        q.add(val);
        return val;
    }
}
