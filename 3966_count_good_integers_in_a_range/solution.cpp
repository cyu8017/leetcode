// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

#include <cmath>
#include <functional>
#include <map>
#include <string>
#include <tuple>
#include <vector>

class Solution {
public:
    long long countGoodIntegers(long long l, long long r, int k) {
        auto count = [&](long long bound) -> long long {
            if (bound <= 0) return 0;
            std::string digits = std::to_string(bound);
            std::map<std::tuple<int, int, bool>, long long> memo;
            std::function<long long(int, int, bool, bool)> dfs = [&](int position, int previous, bool started, bool tight) -> long long {
                if (position == (int)digits.size()) return started ? 1 : 0;
                auto key = std::make_tuple(position, previous, started);
                if (!tight) {
                    auto it = memo.find(key);
                    if (it != memo.end()) return it->second;
                }
                int limit = tight ? digits[position] - '0' : 9;
                long long result = 0;
                for (int digit = 0; digit <= limit; digit++) {
                    bool nextStarted = started || digit != 0;
                    if (started && std::abs(previous - digit) > k) continue;
                    int nextPrevious = nextStarted ? digit : previous;
                    result += dfs(position + 1, nextPrevious, nextStarted, tight && digit == limit);
                }
                if (!tight) memo[key] = result;
                return result;
            };
            return dfs(0, 0, false, true);
        };
        return count(r) - count(l - 1);
    }
};
