// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

import java.util.*;

class FrequencyTracker {
    private final Map<Integer, Integer> freq = new HashMap<>();
    private final Map<Integer, Integer> count = new HashMap<>();

    public FrequencyTracker() {}

    public void add(int number) {
        int old = freq.getOrDefault(number, 0);
        if (old > 0) count.put(old, count.getOrDefault(old, 0) - 1);
        freq.put(number, old + 1);
        count.put(old + 1, count.getOrDefault(old + 1, 0) + 1);
    }

    public void deleteOne(int number) {
        int old = freq.getOrDefault(number, 0);
        if (old == 0) return;
        count.put(old, count.getOrDefault(old, 0) - 1);
        freq.put(number, old - 1);
        if (old - 1 > 0) count.put(old - 1, count.getOrDefault(old - 1, 0) + 1);
    }

    public boolean hasFrequency(int frequency) {
        return count.getOrDefault(frequency, 0) > 0;
    }
}
