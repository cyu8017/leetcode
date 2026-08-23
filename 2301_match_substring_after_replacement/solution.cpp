// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

#include <string>
#include <vector>
#include <unordered_set>

class Solution {
public:
    bool matchReplacement(std::string s, std::string sub, std::vector<std::vector<char>>& mappings) {
        std::unordered_set<int> allow;
        for (auto& m : mappings) allow.insert((m[0] << 8) | m[1]);
        int n = (int)s.size(), mlen = (int)sub.size();
        for (int i = 0; i + mlen <= n; ++i) {
            bool ok = true;
            for (int j = 0; j < mlen; ++j) {
                char a = s[i + j], b = sub[j];
                if (a == b || allow.count((b << 8) | a)) continue;
                ok = false;
                break;
            }
            if (ok) return true;
        }
        return false;
    }
};
