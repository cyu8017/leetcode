// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

// JavaScript problem; C# stand-in of TimeLimitedCache.
using System;
using System.Collections.Generic;
using System.Diagnostics;

public class TimeLimitedCache {
    class Entry {
        public int Value;
        public long Expire;
    }
    Dictionary<int, Entry> data = new Dictionary<int, Entry>();
    static readonly Stopwatch Sw = Stopwatch.StartNew();

    static long NowMs() => Sw.ElapsedMilliseconds;

    public TimeLimitedCache() {}

    public bool Set(int key, int value, int duration) {
        long now = NowMs();
        bool alive = data.TryGetValue(key, out var e) && e.Expire > now;
        data[key] = new Entry { Value = value, Expire = now + duration };
        return alive;
    }

    public int Get(int key) {
        long now = NowMs();
        if (!data.TryGetValue(key, out var e) || e.Expire <= now) return -1;
        return e.Value;
    }

    public int Count() {
        long now = NowMs();
        int cnt = 0;
        var dead = new List<int>();
        foreach (var kv in data) {
            if (kv.Value.Expire > now) cnt++;
            else dead.Add(kv.Key);
        }
        foreach (int k in dead) data.Remove(k);
        return cnt;
    }
}
