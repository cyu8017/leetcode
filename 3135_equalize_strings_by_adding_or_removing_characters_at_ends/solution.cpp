// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minOperations(std::string initial, std::string target) {
        int m = (int)initial.size(), n = (int)target.size();
        std::vector<std::vector<int>> f(m + 1, std::vector<int>(n + 1));
        int mx = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (initial[i] == target[j]) {
                    f[i + 1][j + 1] = f[i][j] + 1;
                    mx = std::max(mx, f[i + 1][j + 1]);
                }
            }
        }
        return m + n - 2 * mx;
    }
};
