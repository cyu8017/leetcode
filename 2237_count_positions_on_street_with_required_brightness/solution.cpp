// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

#include <vector>
#include <algorithm>

class Solution {
public:
    int meetRequirement(int n, std::vector<std::vector<int>>& lights, std::vector<int>& requirement) {
        std::vector<int> diff(n + 1);
        for (auto& light : lights) {
            int pos = light[0], r = light[1];
            int l = std::max(0, pos - r);
            int rr = std::min(n - 1, pos + r);
            diff[l]++;
            diff[rr + 1]--;
        }
        int ans = 0, cur = 0;
        for (int i = 0; i < n; ++i) {
            cur += diff[i];
            if (cur >= requirement[i]) ans++;
        }
        return ans;
    }
};
