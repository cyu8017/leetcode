// LeetCode 1947 - Maximum Compatibility Score Sum
#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    int maxCompatibilitySum(std::vector<std::vector<int>>& students, std::vector<std::vector<int>>& mentors) {
        int m = (int)students.size();
        std::vector<std::vector<int>> score(m, std::vector<int>(m));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                int s = 0;
                for (int k = 0; k < (int)students[i].size(); k++) s += students[i][k] == mentors[j][k];
                score[i][j] = s;
            }
        }
        std::vector<int> memo(1 << m, -1);
        std::function<int(int, int)> dp = [&](int i, int mask) -> int {
            if (i == m) return 0;
            if (memo[mask] != -1) return memo[mask];
            int best = 0;
            for (int j = 0; j < m; j++) {
                if ((mask & (1 << j)) == 0) best = std::max(best, score[i][j] + dp(i + 1, mask | (1 << j)));
            }
            return memo[mask] = best;
        };
        return dp(0, 0);
    }
};
