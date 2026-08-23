// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> findWinners(std::vector<std::vector<int>>& matches) {
        std::unordered_map<int, int> lose;
        std::unordered_set<int> seen;
        for (auto& m : matches) {
            seen.insert(m[0]);
            seen.insert(m[1]);
            lose[m[1]]++;
        }
        std::vector<int> zero, one;
        for (int p : seen) {
            int L = lose[p];
            if (L == 0) zero.push_back(p);
            else if (L == 1) one.push_back(p);
        }
        std::sort(zero.begin(), zero.end());
        std::sort(one.begin(), one.end());
        return {zero, one};
    }
};
