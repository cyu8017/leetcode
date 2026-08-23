// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

#include <string>
#include <vector>

class Solution {
public:
    int vowelStrings(std::vector<std::string>& words, int left, int right) {
        auto isV = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        int ans = 0;
        for (int i = left; i <= right; ++i) {
            const auto& w = words[i];
            if (isV(w.front()) && isV(w.back())) ans++;
        }
        return ans;
    }
};
