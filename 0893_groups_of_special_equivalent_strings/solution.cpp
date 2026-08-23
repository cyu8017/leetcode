// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int numSpecialEquivGroups(std::vector<std::string>& words) {
        std::unordered_set<std::string> groups;
        for (const auto& w : words) {
            std::string even, odd;
            for (size_t i = 0; i < w.size(); ++i) {
                if (i % 2 == 0) {
                    even.push_back(w[i]);
                } else {
                    odd.push_back(w[i]);
                }
            }
            std::sort(even.begin(), even.end());
            std::sort(odd.begin(), odd.end());
            groups.insert(even + "|" + odd);
        }
        return static_cast<int>(groups.size());
    }
};
