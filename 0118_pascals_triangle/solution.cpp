// LeetCode 0118 - Pascal's Triangle
#include <vector>
class Solution { public: std::vector<std::vector<int>> generate(int numRows) {
    std::vector<std::vector<int>> ans;
    for (int i = 0; i < numRows; ++i) { ans.emplace_back(i + 1, 1);
        for (int j = 1; j < i; ++j) ans[i][j] = ans[i-1][j-1] + ans[i-1][j]; }
    return ans;
} };