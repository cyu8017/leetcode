// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

#include <string>
#include <vector>

class Solution {
public:
    std::string smallestSubsequence(std::string s) {
        std::vector<int> last(26, 0);
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            last[s[i] - 'a'] = i;
        }
        std::string stack;
        std::vector<char> used(26, 0);
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            char ch = s[i];
            if (used[ch - 'a']) {
                continue;
            }
            while (!stack.empty() && ch < stack.back() && last[stack.back() - 'a'] > i) {
                used[stack.back() - 'a'] = 0;
                stack.pop_back();
            }
            stack.push_back(ch);
            used[ch - 'a'] = 1;
        }
        return stack;
    }
};
