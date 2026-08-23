// LeetCode 3946 - Maximum Number Of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maximumSaleItems(std::vector<std::vector<int>>& items, int budget) {
        std::vector<int> f(budget + 1, 0);
        int mn = INT_MAX;
        for (auto& item : items) {
            int factor = item[0], price = item[1];
            mn = std::min(mn, price);
            int cnt = 0;
            for (auto& jItem : items) {
                if (jItem[0] % factor == 0) cnt++;
            }
            for (int j = budget; j >= price; j--) {
                f[j] = std::max(f[j], f[j - price] + cnt);
            }
        }
        int ans = 0;
        for (int i = 0; i <= budget; i++) {
            int extra = (budget - i) / mn;
            ans = std::max(ans, f[i] + extra);
        }
        return ans;
    }
};
