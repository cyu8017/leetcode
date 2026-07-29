// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int numEquivDominoPairs(std::vector<std::vector<int>>& dominoes) {
        std::unordered_map<int, int> count;
        int ans = 0;
        for (const auto& d : dominoes) {
            const int key = std::min(d[0], d[1]) * 10 + std::max(d[0], d[1]);
            ans += count[key]++;
        }
        return ans;
    }
};
