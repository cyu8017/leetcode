// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string orderlyQueue(std::string s, int k) {
        if (k > 1) {
            std::sort(s.begin(), s.end());
            return s;
        }
        std::string best = s;
        for (size_t i = 1; i < s.size(); ++i) {
            best = std::min(best, s.substr(i) + s.substr(0, i));
        }
        return best;
    }
};
