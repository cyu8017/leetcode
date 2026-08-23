// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string lastNonEmptyString(std::string s) {
        int cnt[26] = {}, last[26] = {}, mx = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            int c = s[i] - 'a';
            cnt[c]++;
            last[c] = i;
            mx = std::max(mx, cnt[c]);
        }
        std::string ans;
        for (int i = 0; i < (int)s.size(); i++) {
            int c = s[i] - 'a';
            if (cnt[c] == mx && last[c] == i) ans.push_back(s[i]);
        }
        return ans;
    }
};
