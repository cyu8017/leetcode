// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

#include <string>
#include <unordered_set>

class Solution {
public:
    int countGoodSubstrings(std::string s) {
        if (s.size() < 3) {
            return 0;
        }
        int count = 0;
        for (int i = 0; i + 2 < static_cast<int>(s.size()); i++) {
            std::unordered_set<char> window{s[i], s[i + 1], s[i + 2]};
            if (window.size() == 3) {
                count++;
            }
        }
        return count;
    }
};
