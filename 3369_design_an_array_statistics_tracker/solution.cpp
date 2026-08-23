// LeetCode 3369 - Design an Array Statistics Tracker 
// https://leetcode.com/problems/design-an-array-statistics-tracker/

#include <algorithm>
#include <climits>
#include <cstdint>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class StatisticsTracker {
    std::vector<int> arr;
    long long sum = 0;
    std::unordered_map<int, int> freq;
    int modeFreq = 0;
    std::unordered_set<int> modes;

public:
    StatisticsTracker() {}

    void addNumber(int num) {
        arr.push_back(num);
        sum += num;
        int f = ++freq[num];
        if (f > modeFreq) {
            modeFreq = f;
            modes = {num};
        } else if (f == modeFreq) {
            modes.insert(num);
        }
    }

    void removeFirst() {
        if (arr.empty()) return;
        int num = arr[0];
        arr.erase(arr.begin());
        sum -= num;
        if (--freq[num] == 0) freq.erase(num);
        modeFreq = 0;
        modes.clear();
        for (auto& [v, f] : freq) {
            if (f > modeFreq) {
                modeFreq = f;
                modes = {v};
            } else if (f == modeFreq) {
                modes.insert(v);
            }
        }
    }

    int getMean() {
        if (arr.empty()) return 0;
        return (int)(sum / (long long)arr.size());
    }

    int getMedian() {
        int n = (int)arr.size();
        std::vector<int> tmp = arr;
        std::sort(tmp.begin(), tmp.end());
        if (n % 2 == 1) return tmp[n / 2];
        return tmp[n / 2 - 1];
    }

    int getMode() {
        long long best = LLONG_MAX;
        for (int v : modes) if (v < best) best = v;
        if (best == LLONG_MAX) return 0;
        return (int)best;
    }
};
