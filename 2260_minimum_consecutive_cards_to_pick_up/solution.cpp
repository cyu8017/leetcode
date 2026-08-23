// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int minimumCardPickup(std::vector<int>& cards) {
        std::unordered_map<int, int> last;
        int ans = -1;
        for (int i = 0; i < (int)cards.size(); ++i) {
            auto it = last.find(cards[i]);
            if (it != last.end()) {
                int diff = i - it->second + 1;
                if (ans == -1 || diff < ans) ans = diff;
            }
            last[cards[i]] = i;
        }
        return ans;
    }
};
