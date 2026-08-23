// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

#include <vector>

class Solution {
public:
    long long matrixSumQueries(int n, std::vector<std::vector<int>>& queries) {
        std::vector<char> rowDone(n), colDone(n);
        int rowsLeft = n, colsLeft = n;
        long long ans = 0;
        for (int i = (int)queries.size() - 1; i >= 0; i--) {
            int type = queries[i][0], idx = queries[i][1], val = queries[i][2];
            if (type == 0) {
                if (!rowDone[idx]) {
                    ans += 1LL * val * colsLeft;
                    rowDone[idx] = 1;
                    rowsLeft--;
                }
            } else {
                if (!colDone[idx]) {
                    ans += 1LL * val * rowsLeft;
                    colDone[idx] = 1;
                    colsLeft--;
                }
            }
        }
        return ans;
    }
};
