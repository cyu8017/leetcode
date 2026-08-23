// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

#include <cstdint>
#include <functional>
#include <map>
#include <tuple>
#include <vector>

class Solution {
public:
    int countSequences(std::vector<int>& nums, long long k) {
        int n = (int)nums.size();
        std::map<std::tuple<int, int64_t, int64_t>, int> f;
        auto gcd = [](int64_t a, int64_t b) {
            while (b) {
                int64_t t = a % b;
                a = b;
                b = t;
            }
            return a;
        };
        std::function<int(int, int64_t, int64_t)> dfs = [&](int i, int64_t p, int64_t q) {
            if (i == n) return (p == k && q == 1) ? 1 : 0;
            auto key = std::make_tuple(i, p, q);
            if (f.count(key)) return f[key];
            int res = dfs(i + 1, p, q);
            int64_t x = nums[i];
            int64_t g1 = gcd(p * x, q);
            res += dfs(i + 1, (p * x) / g1, q / g1);
            int64_t g2 = gcd(p, q * x);
            res += dfs(i + 1, p / g2, (q * x) / g2);
            return f[key] = res;
        };
        return dfs(0, 1, 1);
    }
};
