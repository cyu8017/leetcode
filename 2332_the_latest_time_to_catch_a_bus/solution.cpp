// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int latestTimeCatchTheBus(std::vector<int>& buses, std::vector<int>& passengers, int capacity) {
        std::sort(buses.begin(), buses.end());
        std::sort(passengers.begin(), passengers.end());
        int pos = 0;
        for (int bi = 0; bi < (int)buses.size(); bi++) {
            int bus = buses[bi];
            int cap = capacity;
            while (cap > 0 && pos < (int)passengers.size() && passengers[pos] <= bus) {
                pos++;
                cap--;
            }
            if (bi == (int)buses.size() - 1) {
                int cand = bus;
                if (cap == 0) {
                    cand = passengers[pos - 1];
                }
                std::unordered_set<int> taken(passengers.begin(), passengers.end());
                while (taken.count(cand)) {
                    cand--;
                }
                return cand;
            }
        }
        return -1;
    }
};
