// LeetCode 3193 - Count the Number of Inversions
// https://leetcode.com/problems/count-the-number-of-inversions/

#include <vector>
#include <algorithm>

class Solution {
public:
    int numberOfPermutations(int n, std::vector<std::vector<int>>& requirements) {
        std::vector<int> req(n, -1);
        for (auto& r : requirements) req[r[0]] = r[1];
        if (req[0] > 0) return 0;
        req[0] = 0;
        int m = *std::max_element(req.begin(), req.end());
        const int mod = 1e9 + 7;
        std::vector<std::vector<int>> f(n, std::vector<int>(m + 1));
        f[0][0] = 1;
        for (int i = 1; i < n; i++) {
            int l = 0, r = m;
            if (req[i] >= 0) l = r = req[i];
            for (int j = l; j <= r; j++) {
                for (int k = 0; k <= std::min(i, j); k++) {
                    f[i][j] = (f[i][j] + f[i - 1][j - k]) % mod;
                }
            }
        }
        return f[n - 1][req[n - 1]];
    }
};
