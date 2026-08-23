// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int uniqueLetterString(std::string s) {
        int n = static_cast<int>(s.size());
        std::unordered_map<char, std::vector<int>> last;
        for (char ch : s) {
            if (!last.count(ch)) {
                last[ch] = {-1};
            }
        }
        for (int i = 0; i < n; ++i) {
            last[s[i]].push_back(i);
        }
        for (auto& [_, indices] : last) {
            indices.push_back(n);
        }
        int ans = 0;
        for (auto& [_, indices] : last) {
            for (size_t k = 1; k + 1 < indices.size(); ++k) {
                ans += (indices[k] - indices[k - 1]) * (indices[k + 1] - indices[k]);
            }
        }
        return ans;
    }
};
