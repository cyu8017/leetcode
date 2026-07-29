// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

#include <string>
#include <vector>

class Solution {
public:
    int countCharacters(std::vector<std::string>& words, std::string chars) {
        int avail[26] = {};
        for (char ch : chars) ++avail[ch - 'a'];
        int ans = 0;
        for (const auto& word : words) {
            int need[26] = {};
            bool ok = true;
            for (char ch : word) {
                if (++need[ch - 'a'] > avail[ch - 'a']) { ok = false; break; }
            }
            if (ok) ans += static_cast<int>(word.size());
        }
        return ans;
    }
};
