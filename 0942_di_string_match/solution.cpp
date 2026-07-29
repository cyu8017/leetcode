// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> diStringMatch(std::string s) {
        int lo = 0, hi = (int)s.size();
        std::vector<int> ans;
        for (char ch : s) {
            if (ch == 'I') ans.push_back(lo++);
            else ans.push_back(hi--);
        }
        ans.push_back(lo);
        return ans;
    }
};
