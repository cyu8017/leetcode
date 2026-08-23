// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::string removeSubstring(std::string s, int k) {
        std::vector<std::pair<char, int>> stk;
        for (char c : s) {
            if (!stk.empty() && stk.back().first == c) stk.back().second++;
            else stk.push_back({c, 1});
            if (c == ')' && stk.size() > 1) {
                auto& top = stk.back();
                auto& prev = stk[stk.size() - 2];
                if (top.second == k && prev.second >= k) {
                    stk.pop_back();
                    prev.second -= k;
                    if (prev.second == 0) stk.pop_back();
                }
            }
        }
        std::string res;
        for (auto& [ch, count] : stk) {
            res.append(count, ch);
        }
        return res;
    }
};
