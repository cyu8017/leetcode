// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

using System.Collections.Generic;

public class Router {
    int lim;
    HashSet<long> vis = new HashSet<long>();
    LinkedList<int[]> q = new LinkedList<int[]>();
    Dictionary<int, int> idx = new Dictionary<int, int>();
    Dictionary<int, List<int>> d = new Dictionary<int, List<int>>();

    long F(int a, int b, int c) {
        return ((long)a << 46) | ((long)b << 29) | (long)c;
    }

    public Router(int memoryLimit) {
        lim = memoryLimit;
    }

    public bool AddPacket(int source, int destination, int timestamp) {
        long x = F(source, destination, timestamp);
        if (vis.Contains(x)) return false;
        vis.Add(x);
        if (q.Count >= lim) ForwardPacket();
        q.AddLast(new int[] { source, destination, timestamp });
        if (!d.ContainsKey(destination)) d[destination] = new List<int>();
        d[destination].Add(timestamp);
        return true;
    }

    public int[] ForwardPacket() {
        if (q.Count == 0) return new int[0];
        int[] packet = q.First.Value;
        q.RemoveFirst();
        int s = packet[0], dest = packet[1], t = packet[2];
        vis.Remove(F(s, dest, t));
        if (!idx.ContainsKey(dest)) idx[dest] = 0;
        idx[dest]++;
        return new int[] { s, dest, t };
    }

    public int GetCount(int destination, int startTime, int endTime) {
        if (!d.ContainsKey(destination)) return 0;
        List<int> ls = d[destination];
        int k = idx.ContainsKey(destination) ? idx[destination] : 0;
        int it1 = LowerBound(ls, k, startTime);
        int it2 = LowerBound(ls, k, endTime + 1);
        return it2 - it1;
    }

    static int LowerBound(List<int> a, int from, int target) {
        int lo = from, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
