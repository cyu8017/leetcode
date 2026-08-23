// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

using System.Collections.Generic;

public class TimeMap {
    private readonly Dictionary<string, List<(int time, string value)>> store = new();

    public TimeMap() {}

    public void Set(string key, string value, int timestamp) {
        if (!store.ContainsKey(key)) store[key] = new List<(int, string)>();
        store[key].Add((timestamp, value));
    }

    public string Get(string key, int timestamp) {
        if (!store.TryGetValue(key, out var arr)) return "";
        int lo = 0, hi = arr.Count - 1, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid].time <= timestamp) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans < 0 ? "" : arr[ans].value;
    }
}
