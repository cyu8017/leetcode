// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

using System.Collections.Generic;
using System.Linq;

public class LogSystem {
    private readonly List<(int id, string timestamp)> logs = new();
    private readonly Dictionary<string, int> granularityIndex = new() {
        ["Year"] = 4, ["Month"] = 7, ["Day"] = 10,
        ["Hour"] = 13, ["Minute"] = 16, ["Second"] = 19,
    };

    public LogSystem() {}

    public void Put(int id, string timestamp) => logs.Add((id, timestamp));

    public IList<int> Retrieve(string start, string end, string granularity) {
        int index = granularityIndex[granularity];
        string startKey = start.Substring(0, index);
        string endKey = end.Substring(0, index);
        var matched = new List<(string timestamp, int id)>();
        foreach (var (logId, timestamp) in logs) {
            string key = timestamp.Substring(0, index);
            if (string.CompareOrdinal(startKey, key) <= 0 && string.CompareOrdinal(key, endKey) <= 0) {
                matched.Add((timestamp, logId));
            }
        }
        matched.Sort();
        return matched.Select(m => m.id).ToList();
    }
}
