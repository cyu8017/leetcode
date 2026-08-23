// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestBalanced(std::string s) {
        int cnt0 = 0;
        for (char c : s) if (c == '0') cnt0++;
        int cnt1 = (int)s.size() - cnt0;
        std::unordered_map<int, std::vector<int>> pos;
        pos[0].push_back(-1);
        int ans = 0, pre = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            if (s[i] == '1') pre++;
            else pre--;
            pos[pre].push_back(i);
            ans = std::max(ans, i - pos[pre][0]);
            if (pos.count(pre - 2)) {
                auto& p = pos[pre - 2];
                if ((i - p[0] - 2) / 2 < cnt0) ans = std::max(ans, i - p[0]);
                else if ((int)p.size() > 1) ans = std::max(ans, i - p[1]);
            }
            if (pos.count(pre + 2)) {
                auto& p = pos[pre + 2];
                if ((i - p[0] - 2) / 2 < cnt1) ans = std::max(ans, i - p[0]);
                else if ((int)p.size() > 1) ans = std::max(ans, i - p[1]);
            }
        }
        return ans;
    }
};
