// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::string bestHand(std::vector<int>& ranks, std::vector<char>& suits) {
        if (suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4]) {
            return "Flush";
        }
        std::unordered_map<int, int> cnt;
        int best = 0;
        for (int r : ranks) {
            best = std::max(best, ++cnt[r]);
        }
        if (best >= 3) return "Three of a Kind";
        if (best == 2) return "Pair";
        return "High Card";
    }
};
