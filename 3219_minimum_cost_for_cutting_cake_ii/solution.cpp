// LeetCode 3219 - Minimum Cost for Cutting Cake II
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long minimumCost(int m, int n, std::vector<int>& horizontalCut, std::vector<int>& verticalCut) {
        std::sort(horizontalCut.rbegin(), horizontalCut.rend());
        std::sort(verticalCut.rbegin(), verticalCut.rend());
        int i = 0, j = 0, h = 1, v = 1;
        long long ans = 0;
        while (i < m - 1 || j < n - 1) {
            if (j == n - 1 || (i < m - 1 && horizontalCut[i] > verticalCut[j])) {
                ans += 1LL * horizontalCut[i] * v;
                h++; i++;
            } else {
                ans += 1LL * verticalCut[j] * h;
                v++; j++;
            }
        }
        return ans;
    }
};
