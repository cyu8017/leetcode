// LeetCode 1396 - Design Underground System
// https://leetcode.com/problems/design-underground-system/

using System.Collections.Generic;
public class UndergroundSystem {
    Dictionary<int, (string, int)> ins = new Dictionary<int, (string, int)>();
    Dictionary<(string, string), (long, int)> stats = new Dictionary<(string, string), (long, int)>();
    public UndergroundSystem() {}
    public void CheckIn(int id, string stationName, int t) { ins[id] = (stationName, t); }
    public void CheckOut(int id, string stationName, int t) {
        var (start, begin) = ins[id]; ins.Remove(id);
        var key = (start, stationName);
        var (total, count) = stats.ContainsKey(key) ? stats[key] : (0L, 0);
        stats[key] = (total + t - begin, count + 1);
    }
    public double GetAverageTime(string startStation, string endStation) {
        var (total, count) = stats[(startStation, endStation)];
        return (double)total / count;
    }
}
