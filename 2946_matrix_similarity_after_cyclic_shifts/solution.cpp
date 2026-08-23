// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

#include <vector>

class Solution {
public:
    bool areSimilar(std::vector<std::vector<int>>& mat, int k) {
        int m = (int)mat.size(), n = (int)mat[0].size();
        for (int i = 0; i < m; i++) {
            int shift;
            if (i % 2 == 0) {
                shift = n - (k % n);
                if (shift == n) shift = 0;
            } else {
                shift = k % n;
            }
            for (int j = 0; j < n; j++)
                if (mat[i][j] != mat[i][(j + shift) % n]) return false;
        }
        return true;
    }
};
