// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int prefixConnected(std::vector<std::string>& words, int k) {
        std::unordered_map<std::string, int> cnt;
        for (auto& w : words) {
            if ((int)w.size() >= k) cnt[w.substr(0, k)]++;
        }
        int ans = 0;
        for (auto& [_, v] : cnt) if (v > 1) ans++;
        return ans;
    }
};
