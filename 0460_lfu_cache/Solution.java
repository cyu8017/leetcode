// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class LFUCache {
    private final int capacity;
    private int minFreq;
    private final Map<Integer, Integer> keyValues = new HashMap<>();
    private final Map<Integer, Integer> keyFreqs = new HashMap<>();
    private final Map<Integer, List<Integer>> freqKeys = new HashMap<>();

    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.minFreq = 0;
    }

    private void touch(int key) {
        int freq = keyFreqs.get(key);
        List<Integer> bucket = freqKeys.get(freq);
        bucket.remove(Integer.valueOf(key));
        if (bucket.isEmpty() && freq == minFreq) {
            minFreq++;
        }
        keyFreqs.put(key, freq + 1);
        freqKeys.computeIfAbsent(freq + 1, ignored -> new ArrayList<>()).add(key);
    }

    public int get(int key) {
        if (!keyValues.containsKey(key)) {
            return -1;
        }
        touch(key);
        return keyValues.get(key);
    }

    public void put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        if (keyValues.containsKey(key)) {
            keyValues.put(key, value);
            touch(key);
            return;
        }
        if (keyValues.size() >= capacity) {
            int evict = freqKeys.get(minFreq).remove(0);
            keyValues.remove(evict);
            keyFreqs.remove(evict);
        }
        keyValues.put(key, value);
        keyFreqs.put(key, 1);
        freqKeys.computeIfAbsent(1, ignored -> new ArrayList<>()).add(key);
        minFreq = 1;
    }
}
