// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

#include <vector>

class Solution {
public:
    std::vector<int> findDegrees(std::vector<std::vector<int>>& matrix) {
        std::vector<int> ans(matrix.size(), 0);
        for (int i = 0; i < (int)matrix.size(); i++) {
            for (int x : matrix[i]) ans[i] += x;
        }
        return ans;
    }
};
