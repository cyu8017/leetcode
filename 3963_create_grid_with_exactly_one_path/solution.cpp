// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> createGrid(int m, int n) {
        std::vector<std::string> g(m, std::string(n, '#'));
        for (int j = 0; j < n; j++) g[0][j] = '.';
        for (int i = 0; i < m; i++) g[i][n - 1] = '.';
        return g;
    }
};
