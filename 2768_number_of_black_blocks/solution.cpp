// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

#include <map>
#include <vector>

class Solution {
public:
    std::vector<long long> countBlackBlocks(int m, int n, std::vector<std::vector<int>>& coordinates) {
        std::map<std::pair<int, int>, int> cnt;
        for (auto& c : coordinates) {
            int x = c[0], y = c[1];
            for (int i = x - 1; i <= x; i++) {
                for (int j = y - 1; j <= y; j++) {
                    if (i >= 0 && j >= 0 && i < m - 1 && j < n - 1) cnt[{i, j}]++;
                }
            }
        }
        std::vector<long long> ans(5, 0);
        ans[0] = 1LL * (m - 1) * (n - 1);
        for (auto& [_, v] : cnt) {
            ans[v]++;
            ans[0]--;
        }
        return ans;
    }
};
