// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/

#include <queue>
#include <string>

class Solution {
public:
    std::string predictPartyVictory(std::string senate) {
        std::queue<int> radiant;
        std::queue<int> dire;
        const int n = static_cast<int>(senate.size());
        for (int i = 0; i < n; ++i) {
            if (senate[i] == 'R') {
                radiant.push(i);
            } else {
                dire.push(i);
            }
        }
        while (!radiant.empty() && !dire.empty()) {
            const int r = radiant.front();
            radiant.pop();
            const int d = dire.front();
            dire.pop();
            if (r < d) {
                radiant.push(r + n);
            } else {
                dire.push(d + n);
            }
        }
        return radiant.empty() ? "Dire" : "Radiant";
    }
};
