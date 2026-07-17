// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maximumBeauty(std::vector<int>& flowers) {
        std::unordered_map<int, int> first;
        std::vector<long long> prefix(flowers.size() + 1, 0);
        for (int i = 0; i < (int)flowers.size(); i++) {
            prefix[i + 1] = prefix[i] + std::max(flowers[i], 0);
        }
        long long best = LLONG_MIN;
        for (int i = 0; i < (int)flowers.size(); i++) {
            int value = flowers[i];
            auto it = first.find(value);
            if (it != first.end()) {
                int left = it->second;
                long long between = prefix[i] - prefix[left + 1];
                best = std::max(best, (long long)flowers[left] + flowers[i] + between);
            } else {
                first[value] = i;
            }
        }
        return (int)best;
    }
};
