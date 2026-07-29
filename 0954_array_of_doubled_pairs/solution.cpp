// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

#include <algorithm>
#include <cmath>
#include <map>
#include <vector>

class Solution {
public:
    bool canReorderDoubled(std::vector<int>& arr) {
        std::map<int, int> count;
        for (int x : arr) count[x]++;
        std::vector<int> keys;
        for (auto& [k, _] : count) keys.push_back(k);
        std::sort(keys.begin(), keys.end(), [](int a, int b) {
            return std::abs(a) < std::abs(b);
        });
        for (int x : keys) {
            if (count[x] == 0) continue;
            if (count[2 * x] < count[x]) return false;
            count[2 * x] -= count[x];
        }
        return true;
    }
};
