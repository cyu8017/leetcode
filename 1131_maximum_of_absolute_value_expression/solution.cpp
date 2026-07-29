// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxAbsValExpr(std::vector<int>& arr1, std::vector<int>& arr2) {
        const int n = static_cast<int>(arr1.size());
        int ans = 0;
        const int signs[4][2] = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        for (const auto& pq : signs) {
            int best = pq[0] * arr1[0] + pq[1] * arr2[0];
            for (int i = 1; i < n; ++i) {
                const int cur = pq[0] * arr1[i] + pq[1] * arr2[i] + i;
                ans = std::max(ans, cur - best);
                best = std::min(best, cur);
            }
        }
        return ans;
    }
};
