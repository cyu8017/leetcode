// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

#include <string>
#include <vector>

class Solution {
public:
    bool checkDistances(std::string s, std::vector<int>& distance) {
        std::vector<int> first(26, -1);
        for (int i = 0; i < (int)s.size(); i++) {
            int c = s[i] - 'a';
            if (first[c] == -1) {
                first[c] = i;
            } else if (i - first[c] - 1 != distance[c]) {
                return false;
            }
        }
        return true;
    }
};
