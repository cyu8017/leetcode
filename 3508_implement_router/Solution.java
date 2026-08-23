// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Router {
    int lim;
    Set<Long> vis = new HashSet<>();
    ArrayDeque<int[]> q = new ArrayDeque<>();
    Map<Integer, Integer> idx = new HashMap<>();
    Map<Integer, List<Integer>> d = new HashMap<>();

    long f(int a, int b, int c) {
        return ((long) a << 46) | ((long) b << 29) | (long) c;
    }

    public Router(int memoryLimit) {
        lim = memoryLimit;
    }

    public boolean addPacket(int source, int destination, int timestamp) {
        long x = f(source, destination, timestamp);
        if (vis.contains(x)) return false;
        vis.add(x);
        if (q.size() >= lim) forwardPacket();
        q.addLast(new int[] {source, destination, timestamp});
        d.computeIfAbsent(destination, k -> new ArrayList<>()).add(timestamp);
        return true;
    }

    public int[] forwardPacket() {
        if (q.isEmpty()) return new int[0];
        int[] packet = q.pollFirst();
        int s = packet[0], dest = packet[1], t = packet[2];
        vis.remove(f(s, dest, t));
        idx.put(dest, idx.getOrDefault(dest, 0) + 1);
        return new int[] {s, dest, t};
    }

    public int getCount(int destination, int startTime, int endTime) {
        List<Integer> ls = d.get(destination);
        if (ls == null) return 0;
        int k = idx.getOrDefault(destination, 0);
        return lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime);
    }

    static int lowerBound(List<Integer> a, int from, int target) {
        int lo = from, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
