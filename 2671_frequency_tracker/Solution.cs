// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

using System.Collections.Generic;

public class FrequencyTracker {
    Dictionary<int, int> freq = new Dictionary<int, int>();
    Dictionary<int, int> count = new Dictionary<int, int>();

    public FrequencyTracker() {}

    public void Add(int number) {
        freq.TryGetValue(number, out int old);
        if (old > 0) {
            count.TryGetValue(old, out int c);
            count[old] = c - 1;
        }
        freq[number] = old + 1;
        count.TryGetValue(old + 1, out int c2);
        count[old + 1] = c2 + 1;
    }

    public void DeleteOne(int number) {
        freq.TryGetValue(number, out int old);
        if (old == 0) return;
        count.TryGetValue(old, out int c);
        count[old] = c - 1;
        freq[number] = old - 1;
        if (old - 1 > 0) {
            count.TryGetValue(old - 1, out int c2);
            count[old - 1] = c2 + 1;
        }
    }

    public bool HasFrequency(int frequency) {
        return count.TryGetValue(frequency, out int c) && c > 0;
    }
}
