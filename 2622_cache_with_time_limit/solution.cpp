// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

#include <chrono>
#include <unordered_map>

// JavaScript problem; C++ stand-in of TimeLimitedCache.
class TimeLimitedCache {
    struct Entry {
        int value = 0;
        long long expire = 0;
    };
    std::unordered_map<int, Entry> data;

    static long long nowMs() {
        using namespace std::chrono;
        return duration_cast<milliseconds>(steady_clock::now().time_since_epoch()).count();
    }

public:
    TimeLimitedCache() {}

    bool set(int key, int value, int duration) {
        long long now = nowMs();
        auto it = data.find(key);
        bool alive = it != data.end() && it->second.expire > now;
        data[key] = {value, now + duration};
        return alive;
    }

    int get(int key) {
        long long now = nowMs();
        auto it = data.find(key);
        if (it == data.end() || it->second.expire <= now) return -1;
        return it->second.value;
    }

    int count() {
        long long now = nowMs();
        int cnt = 0;
        for (auto it = data.begin(); it != data.end();) {
            if (it->second.expire > now) {
                cnt++;
                ++it;
            } else {
                it = data.erase(it);
            }
        }
        return cnt;
    }
};
