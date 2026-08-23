// LeetCode 1553 - Minimum Number of Days to Eat N Oranges
// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

#include <algorithm>
#include <unordered_map>

class Solution {
public:
    int minDays(int n) {
        return dp(n);
    }

private:
    std::unordered_map<int, int> memo;

    int dp(int x) {
        if (x <= 1) {
            return x;
        }
        auto it = memo.find(x);
        if (it != memo.end()) {
            return it->second;
        }
        return memo[x] = 1 + std::min(x % 2 + dp(x / 2), x % 3 + dp(x / 3));
    }
};
