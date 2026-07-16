// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

#include <algorithm>
#include <unordered_map>
#include <vector>

class LFUCache {
    int capacity_;
    int minFreq_;
    std::unordered_map<int, int> keyValues_;
    std::unordered_map<int, int> keyFreqs_;
    std::unordered_map<int, std::vector<int>> freqKeys_;

    void touch(int key) {
        const int freq = keyFreqs_[key];
        auto& bucket = freqKeys_[freq];
        const auto it = std::find(bucket.begin(), bucket.end(), key);
        if (it != bucket.end()) {
            bucket.erase(it);
        }
        if (bucket.empty() && freq == minFreq_) {
            ++minFreq_;
        }
        keyFreqs_[key] = freq + 1;
        freqKeys_[freq + 1].push_back(key);
    }

public:
    LFUCache(int capacity) : capacity_(capacity), minFreq_(0) {}

    int get(int key) {
        if (!keyValues_.count(key)) {
            return -1;
        }
        touch(key);
        return keyValues_[key];
    }

    void put(int key, int value) {
        if (capacity_ == 0) {
            return;
        }
        if (keyValues_.count(key)) {
            keyValues_[key] = value;
            touch(key);
            return;
        }
        if (static_cast<int>(keyValues_.size()) >= capacity_) {
            const int evict = freqKeys_[minFreq_].front();
            freqKeys_[minFreq_].erase(freqKeys_[minFreq_].begin());
            keyValues_.erase(evict);
            keyFreqs_.erase(evict);
        }
        keyValues_[key] = value;
        keyFreqs_[key] = 1;
        freqKeys_[1].push_back(key);
        minFreq_ = 1;
    }
};
