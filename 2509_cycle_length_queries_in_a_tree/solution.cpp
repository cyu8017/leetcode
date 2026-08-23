// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

#include <vector>

class Solution {
public:
    std::vector<int> cycleLengthQueries(int n, std::vector<std::vector<int>>& queries) {
        (void)n;
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int a = queries[i][0], b = queries[i][1];
            int steps = 0;
            while (a != b) {
                if (a > b) a /= 2;
                else b /= 2;
                steps++;
            }
            ans[i] = steps + 1;
        }
        return ans;
    }
};
