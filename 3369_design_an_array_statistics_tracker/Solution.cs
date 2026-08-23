// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

using System;
using System.Collections.Generic;

public class StatisticsTracker {
    List<int> arr = new List<int>();
    long sum = 0;
    Dictionary<int, int> freq = new Dictionary<int, int>();
    int modeFreq = 0;
    HashSet<int> modes = new HashSet<int>();

    public StatisticsTracker() {}

    public void AddNumber(int num) {
        arr.Add(num);
        sum += num;
        if (!freq.ContainsKey(num)) freq[num] = 0;
        int f = ++freq[num];
        if (f > modeFreq) {
            modeFreq = f;
            modes = new HashSet<int> { num };
        } else if (f == modeFreq) {
            modes.Add(num);
        }
    }

    public void RemoveFirst() {
        if (arr.Count == 0) return;
        int num = arr[0];
        arr.RemoveAt(0);
        sum -= num;
        if (--freq[num] == 0) freq.Remove(num);
        modeFreq = 0;
        modes.Clear();
        foreach (var kv in freq) {
            if (kv.Value > modeFreq) {
                modeFreq = kv.Value;
                modes = new HashSet<int> { kv.Key };
            } else if (kv.Value == modeFreq) {
                modes.Add(kv.Key);
            }
        }
    }

    public int GetMean() {
        if (arr.Count == 0) return 0;
        return (int)(sum / arr.Count);
    }

    public int GetMedian() {
        int n = arr.Count;
        var tmp = new List<int>(arr);
        tmp.Sort();
        if (n % 2 == 1) return tmp[n / 2];
        return tmp[n / 2 - 1];
    }

    public int GetMode() {
        long best = long.MaxValue;
        foreach (int v in modes) if (v < best) best = v;
        if (best == long.MaxValue) return 0;
        return (int)best;
    }
}
