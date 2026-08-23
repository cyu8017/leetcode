// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> maximumCoins(std::vector<int>& heroes, std::vector<int>& monsters, std::vector<int>& coins) {
        int n = (int)monsters.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b) { return monsters[a] < monsters[b]; });
        std::vector<long long> pref(n + 1);
        std::vector<int> ms(n);
        for (int i = 0; i < n; i++) {
            ms[i] = monsters[idx[i]];
            pref[i + 1] = pref[i] + coins[idx[i]];
        }
        std::vector<long long> ans(heroes.size());
        for (int i = 0; i < (int)heroes.size(); i++) {
            int p = (int)(std::upper_bound(ms.begin(), ms.end(), heroes[i]) - ms.begin());
            ans[i] = pref[p];
        }
        return ans;
    }
};
