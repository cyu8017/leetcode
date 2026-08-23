// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> maximumSubarrayXor(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> f(n, std::vector<int>(n));
        for (int i = 0; i < n; i++) f[i][i] = nums[i];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                f[i][j] = f[i][j - 1] ^ f[i + 1][j];
            }
        }
        std::vector<std::vector<int>> best(n, std::vector<int>(n));
        for (int i = 0; i < n; i++) best[i][i] = f[i][i];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                best[i][j] = std::max({f[i][j], best[i][j - 1], best[i + 1][j]});
            }
        }
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) ans[i] = best[queries[i][0]][queries[i][1]];
        return ans;
    }
};
