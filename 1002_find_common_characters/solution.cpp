// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

#include <algorithm>
#include <climits>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> commonChars(std::vector<std::string>& words) {
        int common[26];
        std::fill(common, common + 26, INT_MAX);
        for (const auto& w : words) {
            int cnt[26] = {};
            for (char ch : w) cnt[ch - 'a']++;
            for (int i = 0; i < 26; ++i) common[i] = std::min(common[i], cnt[i]);
        }
        std::vector<std::string> ans;
        for (int i = 0; i < 26; ++i) {
            for (int t = 0; t < common[i]; ++t) {
                ans.push_back(std::string(1, static_cast<char>('a' + i)));
            }
        }
        return ans;
    }
};

