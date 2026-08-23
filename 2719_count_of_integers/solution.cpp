// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

#include <string>
#include <functional>
#include <map>
#include <array>

class Solution {
public:
    int count(std::string num1, std::string num2, int min_sum, int max_sum) {
        const int MOD = 1000000007;
        auto dec = [](std::string s) {
            int i = (int)s.size() - 1;
            while (i >= 0 && s[i] == '0') { s[i] = '9'; i--; }
            if (i >= 0) s[i]--;
            int j = 0;
            while (j < (int)s.size() - 1 && s[j] == '0') j++;
            return s.substr(j);
        };
        auto dp = [&](std::string s) {
            int n = (int)s.size();
            std::map<std::array<int,3>, int> memo;
            std::function<int(int,int,bool)> dfs = [&](int pos, int sum, bool tight) -> int {
                if (sum > max_sum) return 0;
                if (pos == n) return sum >= min_sum ? 1 : 0;
                std::array<int,3> key = {pos, sum, tight ? 1 : 0};
                if (memo.count(key)) return memo[key];
                int up = tight ? s[pos] - '0' : 9;
                int res = 0;
                for (int d = 0; d <= up; d++)
                    res = (res + dfs(pos + 1, sum + d, tight && d == up)) % MOD;
                return memo[key] = res;
            };
            return dfs(0, 0, true);
        };
        return (dp(num2) - dp(dec(num1)) + MOD) % MOD;
    }
};
