// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minXor(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> g(n + 1);
        for (int i = 1; i <= n; i++) g[i] = g[i - 1] ^ nums[i - 1];
        const int inf = INT_MAX / 2;
        std::vector<std::vector<int>> f(n + 1, std::vector<int>(k + 1, inf));
        f[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= std::min(i, k); j++) {
                for (int h = j - 1; h < i; h++) {
                    f[i][j] = std::min(f[i][j], std::max(f[h][j - 1], g[i] ^ g[h]));
                }
            }
        }
        return f[n][k];
    }
};
