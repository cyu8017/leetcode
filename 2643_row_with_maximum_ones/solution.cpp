// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

#include <vector>

class Solution {
public:
    std::vector<int> rowAndMaximumOnes(std::vector<std::vector<int>>& mat) {
        int bestRow = 0, bestCnt = -1;
        for (int i = 0; i < (int)mat.size(); i++) {
            int cnt = 0;
            for (int v : mat[i]) cnt += v;
            if (cnt > bestCnt) { bestCnt = cnt; bestRow = i; }
        }
        return {bestRow, bestCnt};
    }
};
