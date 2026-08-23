// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

#include <string>
#include <vector>

class Solution {
    static int bitWidth(unsigned k) {
        int w = 0;
        while (k) {
            ++w;
            k >>= 1;
        }
        return w;
    }

public:
    std::vector<std::string> createGrid(int k) {
        if (k <= 0) return {};
        int l = bitWidth((unsigned)k);
        int m = 2 * l, n = l + 3;
        std::vector<std::string> result(m, std::string(n, '#'));
        for (int i = 0; i < l; i++) {
            int r = 2 * i;
            result[r][i] = result[r][i + 1] = result[r + 1][i] = result[r + 1][i + 1] = '.';
            if (k & (1 << i)) {
                for (int c = i + 2; c < n; c++) result[r][c] = '.';
            }
        }
        for (int r = 0; r < m; r++) result[r][n - 1] = '.';
        return result;
    }
};
