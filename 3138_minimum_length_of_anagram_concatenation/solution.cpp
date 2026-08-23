// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

#include <string>
#include <array>

class Solution {
public:
    int minAnagramLength(std::string s) {
        int n = (int)s.size();
        std::array<int, 26> cnt{};
        for (char c : s) cnt[c - 'a']++;
        auto check = [&](int k) {
            for (int i = 0; i < n; i += k) {
                std::array<int, 26> cnt1{};
                for (int j = i; j < i + k; j++) cnt1[s[j] - 'a']++;
                for (int j = 0; j < 26; j++) {
                    if (cnt1[j] * (n / k) != cnt[j]) return false;
                }
            }
            return true;
        };
        for (int i = 1; ; i++) {
            if (n % i == 0 && check(i)) return i;
        }
    }
};
