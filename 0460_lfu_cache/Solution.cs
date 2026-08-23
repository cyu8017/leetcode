// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

using System.Collections.Generic;

public class LFUCache {
    private readonly int capacity;
    private int minFreq;
    private readonly Dictionary<int, int> keyValues = new();
    private readonly Dictionary<int, int> keyFreqs = new();
    private readonly Dictionary<int, List<int>> freqKeys = new();

    public LFUCache(int capacity) {
        this.capacity = capacity;
        minFreq = 0;
    }

    private void Touch(int key) {
        int freq = keyFreqs[key];
        List<int> bucket = freqKeys[freq];
        bucket.Remove(key);
        if (bucket.Count == 0 && freq == minFreq) {
            minFreq++;
        }
        int nextFreq = freq + 1;
        keyFreqs[key] = nextFreq;
        if (!freqKeys.TryGetValue(nextFreq, out List<int> nextBucket)) {
            nextBucket = new List<int>();
            freqKeys[nextFreq] = nextBucket;
        }
        nextBucket.Add(key);
    }

    public int Get(int key) {
        if (!keyValues.ContainsKey(key)) {
            return -1;
        }
        Touch(key);
        return keyValues[key];
    }

    public void Put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        if (keyValues.ContainsKey(key)) {
            keyValues[key] = value;
            Touch(key);
            return;
        }
        if (keyValues.Count >= capacity) {
            int evict = freqKeys[minFreq][0];
            freqKeys[minFreq].RemoveAt(0);
            keyValues.Remove(evict);
            keyFreqs.Remove(evict);
        }
        keyValues[key] = value;
        keyFreqs[key] = 1;
        if (!freqKeys.TryGetValue(1, out List<int> bucket)) {
            bucket = new List<int>();
            freqKeys[1] = bucket;
        }
        bucket.Add(key);
        minFreq = 1;
    }
}
