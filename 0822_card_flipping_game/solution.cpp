// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

#include <algorithm>
#include <climits>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int flipgame(std::vector<int>& fronts, std::vector<int>& backs) {
        std::unordered_set<int> same;
        for (size_t i = 0; i < fronts.size(); ++i) {
            if (fronts[i] == backs[i]) {
                same.insert(fronts[i]);
            }
        }
        int best = INT_MAX;
        for (int x : fronts) {
            if (!same.count(x)) {
                best = std::min(best, x);
            }
        }
        for (int x : backs) {
            if (!same.count(x)) {
                best = std::min(best, x);
            }
        }
        return best == INT_MAX ? 0 : best;
    }
};
