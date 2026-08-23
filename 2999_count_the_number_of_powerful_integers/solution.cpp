// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

#include <string>
#include <functional>
#include <map>
#include <utility>

class Solution {
public:
    long long numberOfPowerfulInt(long long start, long long finish, int limit, std::string s) {
        auto count = [&](long long num) -> long long {
            if (num < 0) return 0;
            for (char c : s) if (c - '0' > limit) return 0;
            std::string t = std::to_string(num);
            int n = (int)t.size(), sn = (int)s.size();
            if (n < sn) return 0;
            long long ans = 0;
            for (int length = sn; length < n; length++) {
                int preLen = length - sn;
                if (preLen == 0) {
                    ans += 1;
                } else {
                    long long ways = limit;
                    for (int i = 1; i < preLen; i++) ways *= (limit + 1);
                    ans += ways;
                }
            }
            int pref = n - sn;
            std::function<long long(int, bool, std::map<std::pair<int, int>, long long>&)> dfs =
                [&](int i, bool tight, std::map<std::pair<int, int>, long long>& memo) -> long long {
                if (i == pref) {
                    if (tight) return t.substr(pref) >= s ? 1 : 0;
                    return 1;
                }
                auto key = std::make_pair(i, tight ? 1 : 0);
                auto it = memo.find(key);
                if (it != memo.end()) return it->second;
                int up = tight ? t[i] - '0' : limit;
                if (up > limit) up = limit;
                long long res = 0;
                for (int d = 0; d <= up; d++) {
                    if (i == 0 && d == 0) continue;
                    res += dfs(i + 1, tight && d == (t[i] - '0'), memo);
                }
                return memo[key] = res;
            };
            std::map<std::pair<int, int>, long long> memo;
            ans += dfs(0, true, memo);
            return ans;
        };
        return count(finish) - count(start - 1);
    }
};
