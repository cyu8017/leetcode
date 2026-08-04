// LeetCode 1396 - Design Underground System
// https://leetcode.com/problems/design-underground-system/

import java.util.*;

class UndergroundSystem {
    private Map<Integer, Object[]> ins = new HashMap<>();
    private Map<String, long[]> stats = new HashMap<>();

    public UndergroundSystem() {}

    public void checkIn(int id, String stationName, int t) {
        ins.put(id, new Object[]{stationName, t});
    }

    public void checkOut(int id, String stationName, int t) {
        Object[] in = ins.remove(id);
        String start = (String) in[0];
        int begin = (Integer) in[1];
        String key = start + ">" + stationName;
        long[] st = stats.computeIfAbsent(key, k -> new long[2]);
        st[0] += t - begin;
        st[1]++;
    }

    public double getAverageTime(String startStation, String endStation) {
        long[] st = stats.get(startStation + ">" + endStation);
        return (double) st[0] / st[1];
    }
}
