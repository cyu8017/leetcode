// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

#include <vector>
#include <numeric>
#include <functional>

class Solution {
public:
    int selfDivisiblePermutationCount(int n) {
        int ans = 0;
        std::vector<char> used(n + 1, 0);
        std::function<void(int)> dfs = [&](int pos) {
            if (pos > n) {
                ans++;
                return;
            }
            for (int v = 1; v <= n; v++) {
                if (used[v]) continue;
                if (std::gcd(v, pos) != 1) continue;
                used[v] = 1;
                dfs(pos + 1);
                used[v] = 0;
            }
        };
        dfs(1);
        return ans;
    }
};
