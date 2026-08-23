// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

#include <map>
#include <string>
#include <utility>

class Solution {
public:
    long long beautifulSubstrings(std::string s, int k) {
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        int x = 1;
        while ((x * x) % k != 0) x++;
        std::map<std::pair<int, int>, int> freq;
        freq[{0, 0}] = 1;
        int bal = 0, vowels = 0;
        long long ans = 0;
        for (char ch : s) {
            if (isVowel(ch)) { bal++; vowels++; }
            else bal--;
            auto kk = std::make_pair(bal, vowels % x);
            ans += freq[kk];
            freq[kk]++;
        }
        return ans;
    }
};
