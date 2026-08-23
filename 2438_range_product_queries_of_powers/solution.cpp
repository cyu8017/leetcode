// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

#include <vector>

class Solution {
public:
    std::vector<int> productQueries(int n, std::vector<std::vector<int>>& queries) {
        const int mod = 1000000007;
        std::vector<int> powers;
        for (int bit = 0; bit < 31; bit++) {
            if ((n >> bit) & 1) powers.push_back(1 << bit);
        }
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            long long prod = 1;
            for (int j = queries[i][0]; j <= queries[i][1]; j++) {
                prod = prod * powers[j] % mod;
            }
            ans[i] = (int)prod;
        }
        return ans;
    }
};
