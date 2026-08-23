// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

#include <string>
#include <vector>

class Solution {
public:
    int maximumCostSubstring(std::string s, std::string chars, std::vector<int>& vals) {
        int val[26];
        for (int i = 0; i < 26; ++i) val[i] = i + 1;
        for (size_t i = 0; i < chars.size(); ++i) val[chars[i] - 'a'] = vals[i];
        int best = 0, cur = 0;
        for (char c : s) {
            cur += val[c - 'a'];
            if (cur < 0) cur = 0;
            if (cur > best) best = cur;
        }
        return best;
    }
};
