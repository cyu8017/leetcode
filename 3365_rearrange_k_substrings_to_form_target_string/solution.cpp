// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

#include <string>
#include <unordered_map>

class Solution {
public:
    bool isPossibleToRearrange(std::string s, std::string t, int k) {
        int n = (int)s.size();
        int sz = n / k;
        std::unordered_map<std::string, int> cnt;
        for (int i = 0; i < n; i += sz) {
            cnt[s.substr(i, sz)]++;
            cnt[t.substr(i, sz)]--;
        }
        for (auto& [_, v] : cnt) if (v != 0) return false;
        return true;
    }
};
