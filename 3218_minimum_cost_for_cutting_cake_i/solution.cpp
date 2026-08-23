// LeetCode 3218 - Minimum Cost for Cutting Cake I
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumCost(int m, int n, std::vector<int>& horizontalCut, std::vector<int>& verticalCut) {
        std::sort(horizontalCut.rbegin(), horizontalCut.rend());
        std::sort(verticalCut.rbegin(), verticalCut.rend());
        int i = 0, j = 0, h = 1, v = 1, ans = 0;
        while (i < m - 1 || j < n - 1) {
            if (j == n - 1 || (i < m - 1 && horizontalCut[i] > verticalCut[j])) {
                ans += horizontalCut[i] * v;
                h++; i++;
            } else {
                ans += verticalCut[j] * h;
                v++; j++;
            }
        }
        return ans;
    }
};
