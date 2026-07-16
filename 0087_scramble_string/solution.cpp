// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    bool isScramble(std::string s1, std::string s2) {
        return dfs(s1, s2);
    }

private:
    std::unordered_map<std::string, bool> memo;

    bool dfs(const std::string& a, const std::string& b) {
        std::string key = a + "#" + b;
        if (memo.count(key)) {
            return memo[key];
        }
        if (a == b) {
            return memo[key] = true;
        }
        std::string sa = a, sb = b;
        std::sort(sa.begin(), sa.end());
        std::sort(sb.begin(), sb.end());
        if (sa != sb) {
            return memo[key] = false;
        }

        int n = (int)a.size();
        for (int i = 1; i < n; i++) {
            if (dfs(a.substr(0, i), b.substr(0, i)) && dfs(a.substr(i), b.substr(i))) {
                return memo[key] = true;
            }
            if (dfs(a.substr(0, i), b.substr(n - i)) && dfs(a.substr(i), b.substr(0, n - i))) {
                return memo[key] = true;
            }
        }
        return memo[key] = false;
    }
};
