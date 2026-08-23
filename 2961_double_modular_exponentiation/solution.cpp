// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

#include <vector>

class Solution {
public:
    std::vector<int> getGoodIndices(std::vector<std::vector<int>>& variables, int target) {
        auto modPow = [](long long a, long long b, long long mod) -> long long {
            long long res = 1 % mod;
            a %= mod;
            while (b > 0) {
                if (b & 1) res = res * a % mod;
                a = a * a % mod;
                b >>= 1;
            }
            return res;
        };
        std::vector<int> ans;
        for (int i = 0; i < (int)variables.size(); i++) {
            auto& v = variables[i];
            int a = v[0], b = v[1], c = v[2], m = v[3];
            if (modPow(modPow(a, b, 10), c, m) == target) ans.push_back(i);
        }
        return ans;
    }
};
