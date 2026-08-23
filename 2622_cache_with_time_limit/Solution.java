// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

import java.util.*;

// JavaScript problem; Java stand-in of TimeLimitedCache.
class TimeLimitedCache {
    private static class Entry {
        int value;
        long expire;
        Entry(int value, long expire) {
            this.value = value;
            this.expire = expire;
        }
    }

    private final Map<Integer, Entry> data = new HashMap<>();
    private final long start = System.nanoTime();

    private long nowMs() {
        return (System.nanoTime() - start) / 1_000_000L;
    }

    public TimeLimitedCache() {}

    public boolean set(int key, int value, int duration) {
        long now = nowMs();
        Entry e = data.get(key);
        boolean alive = e != null && e.expire > now;
        data.put(key, new Entry(value, now + duration));
        return alive;
    }

    public int get(int key) {
        long now = nowMs();
        Entry e = data.get(key);
        if (e == null || e.expire <= now) return -1;
        return e.value;
    }

    public int count() {
        long now = nowMs();
        int cnt = 0;
        List<Integer> dead = new ArrayList<>();
        for (Map.Entry<Integer, Entry> kv : data.entrySet()) {
            if (kv.getValue().expire > now) cnt++;
            else dead.add(kv.getKey());
        }
        for (int k : dead) data.remove(k);
        return cnt;
    }
}
