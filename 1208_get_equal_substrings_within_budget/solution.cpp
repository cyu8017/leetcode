// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

#include <algorithm>
#include <cstdlib>
#include <string>

class Solution {
public:
    int equalSubstring(std::string s, std::string t, int maxCost) {
        int left = 0, cost = 0, answer = 0;
        for (int right = 0; right < static_cast<int>(s.size()); ++right) {
            cost += std::abs(s[right] - t[right]);
            while (cost > maxCost) {
                cost -= std::abs(s[left] - t[left]);
                ++left;
            }
            answer = std::max(answer, right - left + 1);
        }
        return answer;
    }
};
