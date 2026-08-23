// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumProcessableQueries(std::vector<int>& nums, std::vector<int>& queries) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> f(n, std::vector<int>(n, 0));
        int m = (int)queries.size();
        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j >= i; j--) {
                if (i > 0) {
                    int t = nums[i - 1] >= queries[f[i - 1][j]] ? 1 : 0;
                    f[i][j] = std::max(f[i][j], f[i - 1][j] + t);
                }
                if (j + 1 < n) {
                    int t = nums[j + 1] >= queries[f[i][j + 1]] ? 1 : 0;
                    f[i][j] = std::max(f[i][j], f[i][j + 1] + t);
                }
                if (f[i][j] == m) return m;
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int t = nums[i] >= queries[f[i][i]] ? 1 : 0;
            ans = std::max(ans, f[i][i] + t);
        }
        return ans;
    }
};
