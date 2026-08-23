// LeetCode 0598 - Range Addition II
// https://leetcode.com/problems/range-addition-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxCount(int m, int n, std::vector<std::vector<int>>& ops) {
        for (const std::vector<int>& op : ops) {
            m = std::min(m, op[0]);
            n = std::min(n, op[1]);
        }
        return m * n;
    }
};
