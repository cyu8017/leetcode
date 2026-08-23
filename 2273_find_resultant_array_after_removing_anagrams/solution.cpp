// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

#include <vector>
#include <string>
#include <array>

class Solution {
public:
    std::vector<std::string> removeAnagrams(std::vector<std::string>& words) {
        auto sig = [](const std::string& w) {
            std::array<int, 26> c{};
            for (char ch : w) c[ch - 'a']++;
            return c;
        };
        std::vector<std::string> ans{words[0]};
        auto prev = sig(words[0]);
        for (size_t i = 1; i < words.size(); ++i) {
            auto cur = sig(words[i]);
            if (cur != prev) {
                ans.push_back(words[i]);
                prev = cur;
            }
        }
        return ans;
    }
};
