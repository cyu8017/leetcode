// LeetCode 0417 - Pacific Atlantic Water Flow
// https://leetcode.com/problems/pacific-atlantic-water-flow/

#include <functional>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty() || heights[0].empty()) {
            return {};
        }

        int rows = (int)heights.size();
        int cols = (int)heights[0].size();
        vector<vector<bool>> pacific(rows, vector<bool>(cols, false));
        vector<vector<bool>> atlantic(rows, vector<bool>(cols, false));

        function<void(int, int, vector<vector<bool>>&, int)> dfs =
            [&](int row, int col, vector<vector<bool>>& visited, int previous) {
                if (row < 0 || row >= rows || col < 0 || col >= cols || visited[row][col] ||
                    heights[row][col] < previous) {
                    return;
                }
                visited[row][col] = true;
                int height = heights[row][col];
                dfs(row + 1, col, visited, height);
                dfs(row - 1, col, visited, height);
                dfs(row, col + 1, visited, height);
                dfs(row, col - 1, visited, height);
            };

        for (int row = 0; row < rows; ++row) {
            dfs(row, 0, pacific, heights[row][0]);
            dfs(row, cols - 1, atlantic, heights[row][cols - 1]);
        }
        for (int col = 0; col < cols; ++col) {
            dfs(0, col, pacific, heights[0][col]);
            dfs(rows - 1, col, atlantic, heights[rows - 1][col]);
        }

        vector<vector<int>> result;
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (pacific[row][col] && atlantic[row][col]) {
                    result.push_back({row, col});
                }
            }
        }

        return result;
    }
};
