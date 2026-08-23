// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

#include <string>
#include <functional>

class Solution {
public:
    int punishmentNumber(int n) {
        auto can = [](int sq, int target) {
            std::string s = std::to_string(sq);
            int m = (int)s.size();
            std::function<bool(int,int)> dfs = [&](int i, int sum) -> bool {
                if (i == m) return sum == target;
                int cur = 0;
                for (int j = i; j < m; j++) {
                    cur = cur * 10 + (s[j] - '0');
                    if (sum + cur > target) break;
                    if (dfs(j + 1, sum + cur)) return true;
                }
                return false;
            };
            return dfs(0, 0);
        };
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int sq = i * i;
            if (can(sq, i)) ans += sq;
        }
        return ans;
    }
};
