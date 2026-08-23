// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int maxPalindromesAfterOperations(std::vector<std::string>& words) {
        int s = 0, mask = 0;
        for (auto& w : words) {
            s += (int)w.size();
            for (char c : w) mask ^= 1 << (c - 'a');
        }
        s -= __builtin_popcount((unsigned)mask);
        std::sort(words.begin(), words.end(), [](const auto& a, const auto& b) {
            return a.size() < b.size();
        });
        int ans = 0;
        for (auto& w : words) {
            s -= (int)w.size() / 2 * 2;
            if (s < 0) break;
            ans++;
        }
        return ans;
    }
};
