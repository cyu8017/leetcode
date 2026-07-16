// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> findAnagrams(std::string s, std::string p) {
        if (p.size() > s.size()) {
            return {};
        }

        std::vector<int> need(26, 0);
        std::vector<int> window(26, 0);
        for (char ch : p) {
            ++need[ch - 'a'];
        }

        std::vector<int> result;
        int left = 0;
        for (int right = 0; right < static_cast<int>(s.size()); ++right) {
            ++window[s[right] - 'a'];
            if (right - left + 1 > static_cast<int>(p.size())) {
                --window[s[left] - 'a'];
                ++left;
            }
            if (window == need) {
                result.push_back(left);
            }
        }
        return result;
    }
};
