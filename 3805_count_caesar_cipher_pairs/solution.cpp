// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countPairs(std::vector<std::string>& words) {
        std::unordered_map<std::string, int> cnt;
        for (auto s : words) {
            int k = 'z' - s[0];
            for (int i = 1; i < (int)s.size(); i++) {
                s[i] = 'a' + (s[i] - 'a' + k) % 26;
            }
            s[0] = 'z';
            cnt[s]++;
        }
        int64_t ans = 0;
        for (auto& [_, v] : cnt) ans += (int64_t)v * (v - 1) / 2;
        return ans;
    }
};
