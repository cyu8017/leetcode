// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> colorRed(int n) {
        std::vector<std::vector<int>> ans;
        for (int i = 1; i <= n; i++) ans.push_back({i, 1});
        for (int i = n % 2 + 2; i <= n; i += 2)
            for (int j = 2; j <= 2 * (n - i) + 2; j++)
                ans.push_back({i, j});
        return ans;
    }
};
