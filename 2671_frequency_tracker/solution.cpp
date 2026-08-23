// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

#include <unordered_map>

class FrequencyTracker {
    std::unordered_map<int, int> freq, count;
public:
    FrequencyTracker() {}
    void add(int number) {
        int old = freq[number];
        if (old > 0) count[old]--;
        freq[number] = old + 1;
        count[old + 1]++;
    }
    void deleteOne(int number) {
        int old = freq[number];
        if (old == 0) return;
        count[old]--;
        freq[number] = old - 1;
        if (old - 1 > 0) count[old - 1]++;
    }
    bool hasFrequency(int frequency) {
        return count[frequency] > 0;
    }
};
