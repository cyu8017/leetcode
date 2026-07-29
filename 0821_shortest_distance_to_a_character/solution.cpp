// LeetCode 0821 - Shortest Distance to a Character
// https://leetcode.com/problems/shortest-distance-to-a-character/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> shortestToChar(std::string s, char c) {
        int n = static_cast<int>(s.size());
        std::vector<int> ans(n);
        int prev = -n;
        for (int i = 0; i < n; ++i) {
            if (s[i] == c) {
                prev = i;
            }
            ans[i] = i - prev;
        }
        prev = 2 * n;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == c) {
                prev = i;
            }
            ans[i] = std::min(ans[i], prev - i);
        }
        return ans;
    }
};
