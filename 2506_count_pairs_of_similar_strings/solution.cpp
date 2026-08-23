// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

#include <array>
#include <map>
#include <string>
#include <vector>

class Solution {
public:
    int similarPairs(std::vector<std::string>& words) {
        std::map<std::array<bool, 26>, int> freq;
        int ans = 0;
        for (auto& w : words) {
            std::array<bool, 26> mask{};
            for (char c : w) mask[c - 'a'] = true;
            ans += freq[mask];
            freq[mask]++;
        }
        return ans;
    }
};
