// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> createGrid(int m, int n, int k) {
        std::vector<std::vector<std::string>> cands;
        if (k == 1) {
            cands.push_back({"."});
        } else if (k == 2) {
            cands.push_back({"..", ".."});
        } else if (k == 3) {
            cands.push_back({"..", "..", ".."});
            cands.push_back({"...", "..."});
        } else if (k == 4) {
            cands.push_back({"..", "..", "..", ".."});
            cands.push_back({"....", "...."});
            cands.push_back({"..#", "...", "#.."});
        }

        for (auto& pat : cands) {
            int pr = (int)pat.size();
            int pc = (int)pat[0].size();
            if (pr > m || pc > n) continue;
            std::vector<std::string> result(m, std::string(n, '#'));
            for (int i = 0; i < pr; i++) {
                for (int j = 0; j < pc; j++) result[i][j] = pat[i][j];
            }
            for (int i = pr; i < m; i++) result[i][pc - 1] = '.';
            for (int j = pc; j < n; j++) result[m - 1][j] = '.';
            return result;
        }
        return {};
    }
};
