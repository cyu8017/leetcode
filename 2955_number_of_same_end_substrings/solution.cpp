// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

#include <array>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> sameEndSubstringCount(std::string s, std::vector<std::vector<int>>& queries) {
        int n = (int)s.size();
        std::vector<std::array<int, 26>> pref(n + 1);
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i];
            pref[i + 1][s[i] - 'a']++;
        }
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int l = queries[qi][0], r = queries[qi][1], total = 0;
            for (int c = 0; c < 26; c++) {
                int cnt = pref[r + 1][c] - pref[l][c];
                total += cnt * (cnt + 1) / 2;
            }
            ans[qi] = total;
        }
        return ans;
    }
};
