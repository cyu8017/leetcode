// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

public class MRUQueue {
    private readonly List<int> q = new List<int>();

    public MRUQueue(int n) {
        for (int i = 1; i <= n; i++) {
            q.Add(i);
        }
    }

    public int Fetch(int k) {
        int val = q[k - 1];
        q.RemoveAt(k - 1);
        q.Add(val);
        return val;
    }
}
