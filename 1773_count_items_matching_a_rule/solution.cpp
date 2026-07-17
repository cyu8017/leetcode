// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/

#include <string>
#include <vector>

class Solution {
public:
    int countMatches(std::vector<std::vector<std::string>>& items, std::string ruleKey,
                     std::string ruleValue) {
        int idx = ruleKey == "type" ? 0 : ruleKey == "color" ? 1 : 2;
        int count = 0;
        for (const auto& item : items) {
            if (item[idx] == ruleValue) {
                count++;
            }
        }
        return count;
    }
};
