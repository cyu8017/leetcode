// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

#include <string>
#include <vector>

class Solution {
public:
    bool haveConflict(std::vector<std::string>& event1, std::vector<std::string>& event2) {
        return event1[0] <= event2[1] && event2[0] <= event1[1];
    }
};
