// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int distinctPoints(std::string s, int k) {
        int n = (int)s.size();
        std::vector<int> f(n + 1), g(n + 1);
        int x = 0, y = 0;
        for (int i = 1; i <= n; i++) {
            char c = s[i - 1];
            if (c == 'U') y++;
            else if (c == 'D') y--;
            else if (c == 'L') x--;
            else x++;
            f[i] = x;
            g[i] = y;
        }
        std::unordered_set<long long> st;
        for (int i = k; i <= n; i++) {
            int a = f[n] - (f[i] - f[i - k]);
            int b = g[n] - (g[i] - g[i - k]);
            long long key = (long long)a * n + b;
            st.insert(key);
        }
        return (int)st.size();
    }
};
