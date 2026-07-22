// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

#include <algorithm>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::string slowestKey(std::vector<int>& releaseTimes, std::string keysPressed) {
        std::pair<int, char> best{releaseTimes[0], keysPressed[0]};
        for (int i = 1; i < static_cast<int>(releaseTimes.size()); ++i) {
            const int duration = releaseTimes[i] - releaseTimes[i - 1];
            best = std::max(best, std::make_pair(duration, keysPressed[i]));
        }
        return std::string(1, best.second);
    }
};
